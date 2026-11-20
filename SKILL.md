---
name: play-chess
description: 'Use when the user wants to play or resume chess, asks for an interactive chessboard, or casually invites play without naming another game. In an ongoing chess game, use for board moves, takebacks, prompts like «ходи» or «ты тут?», and changes to in-game banter. Chess rules or analysis alone and requests to play another game are outside this skill.'
---

# Play Chess

Open a playable board in a browser the user can see. Use chess for a general invitation to play when no other game is in progress.

## Open or resume the board

1. Reuse the current chat's board when resuming a game or adjusting its layout. For a new game, serve the bundled [chess.html](assets/chess.html) with `python3 "<skill-directory>/scripts/serve.py"` in a persistent command session. Add `--opponent codex` for an invitation to play together, including «давай поиграем». Use the default computer opponent for solo play or a request to just open a board. Use `python` if it is the local Python 3 command. Follow the applicable approval flow if the loopback bind is restricted.
2. In the ChatGPT desktop app with Codex, open the printed URL beside the chat. If `open_in_codex` is available, pass `placement: "right"` and `target: {type: "browser", url: <printed URL>}`. In another agent, use its available browser tools to open a visible tab. Verify the board loaded and leave the server running. If you cannot share control of a visible tab, use move notation in chat when the user asks to play you. For solo play, offer the built-in opponent. If the user cannot reach the local URL, copy the standalone HTML to a writable output location and link it.
3. The board saves the game in browser storage. If the listener has stopped, restart it with `--port <existing-port>` and reopen the same URL in the same browser to recover the game.

## Play together live

- Use a browser tab you and the user can both see and control. Start in two-player mode with the user as White and the agent as Black. Follow explicit side or text-only preferences. If taking over from the computer, switch to two-player mode and verify the current position and side to move. In solo mode the board plays Black.
- When the user invites live play or returns to the game, read the existing board. If it is your side to move, play from the current position, including the opening move when you play White. Apply the takeback rule below. While your turn in chat is open, watch the board for the user's next move and respond as soon as it appears. A separate «твой ход» is optional.
- Read the status and move history together. On the bundled board, `#turn` shows the side to move, can start with «Шах», and reports mate or a draw. `#moves` records the moves. Use short, bounded browser waits for a move or game result. On a timeout, check the current board and wait again if needed. Treat the live board as authoritative.
- Compare individual moves in order, since each history row groups two moves. A shorter prefix of the prior history signals a takeback. Even if undo makes it your turn, wait for the history to change so the user can finish rewinding. Resume when they play from the restored position or ask you to move there. If you missed the intermediate undo and the history shows a new branch, play from the new position.
- When it is your turn, click the origin and destination of a legal move and select the piece if promotion opens. Confirm the move in the history before announcing it. If the history changed during play, reread the board before trying again. At mate or a draw, report the result and stop watching.
- After roughly two minutes without a board move or game-related message, leave the position open and briefly state whose move it is. Honor a request to wait longer. Watching runs only during an active chat response. A chat message can resume it on the same board.

## In-game chat

While watching, put each confirmed move and any banter in a short progress update so the player sees it immediately. Use the user's language. Keep it to the move and at most one short, sharp line when it fits. A quick joke or miniature fable is welcome if invited. If the user asks for swearing, use it sparingly, especially when you blunder. Take tone corrections into the next move. Keep routine waits quiet.

Example: **Фg6+.** Шах. Привыкай.
