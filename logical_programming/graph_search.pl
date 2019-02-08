% Knowledge base for a deterministic finite automaton.
% It represents the state transfer function.
edge(s, z2, a).
edge(s, z3, b).
edge(z2, z3, a).
edge(z2, z4, b).
edge(z3, s, a).
edge(z3, z4, b).
edge(z4, s, b).
edge(z4, zakz, a).

% entry point for a query. Determines if a word is element of the
% language L given by the automaton.
isElementOfL([H|T]):- edge(s, X, H), stateChange(X, _, T).

% Determines the changes in the state by the head element of the word
% (the first letter) and calls itself recursively for the next letter.
% Abort condition is reached if the list is empty (-> no letters
% remaining) and returns TRUE, if the reached state is zAkz.
stateChange(STATE, STATEAFTER, [H|T]):- edge(STATE, STATEAFTER, H), stateChange(STATEAFTER, _, T).
stateChange(ENDSTATE, _, []):- ENDSTATE == zakz.
