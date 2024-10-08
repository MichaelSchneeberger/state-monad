from abc import abstractmethod
from typing import Callable

from statemonad.exceptions import StateMonadOperatorException
from statemonad.statemonadtree.nodes import SingleChildStateMonadNode
from statemonad.utils.getstacklines import (
    FrameSummaryMixin,
)


class MapMixin[State, U, ChildU](
    FrameSummaryMixin, SingleChildStateMonadNode[State, U, ChildU]
):
    def __str__(self) -> str:
        return f"map({self.child}, {self.func})"

    @property
    @abstractmethod
    def func(self) -> Callable[[ChildU], U]: ...

    def apply(self, state: State) -> tuple[State, U]:
        state, value = self.child.apply(state)

        try:
            result = self.func(value)

        except StateMonadOperatorException:
            raise

        except Exception:
            raise StateMonadOperatorException(self.to_operator_exception_message())

        return state, result
