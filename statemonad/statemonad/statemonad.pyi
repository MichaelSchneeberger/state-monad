from typing import Callable, override, Generator

from statemonad.statemonadtree.nodes import StateMonadNode

class StateMonad[State, U](StateMonadNode[State, U]):
    # used for the donotation.do notation
    def __iter__(self) -> Generator[None, None, U]: ...
    @override
    def apply(self, state: State) -> tuple[State, U]: ...
    def copy(self, /, **changes) -> StateMonad[State, U]: ...

    # operations
    ############

    def flat_map[V](
        self, func: Callable[[U], StateMonad[State, V]]
    ) -> StateMonad[State, V]: ...
    def get(self) -> StateMonad[State, State]: ...
    def map[V](self, func: Callable[[U], V]) -> StateMonad[State, V]: ...
    def zip[V](self, other: StateMonad[State, V]) -> StateMonad[State, tuple[U, V]]: ...
    def put(self, state: State) -> StateMonad[State, U]: ...
