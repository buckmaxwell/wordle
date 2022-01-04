# Wordle Solver - CLI mode

Run `python solve.py`

Come up with a 5 letter word. Troll for example.

```sh
I will guess wound
How did I do?: -!---
I will guess other
How did I do?: !!--!
I will guess sport
How did I do?: --x!!
I will guess troll
```
For the how did I do prompts,

`-` means letter is not used.
`!` letter is used, but not in this place.
`x` letter is used and is in the correct place.

# Wordle Solver - Automatic Mode

1. Install Playwright
- Run `pip install playwright`
- Run `playwright install`

2. Run the automatic solver
- Run `python automatic-solve.py`
