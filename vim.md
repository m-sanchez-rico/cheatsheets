
| **Category**                  | **Command**                                    | **Description**                                          |
|-------------------------------|------------------------------------------------|----------------------------------------------------------|
| **Installation**              | vim, nvim                                      | Different versions of the text editor                    |
| **Exit**                      | `:q`                                           | Quit                                                     |
|                               | `:!q`                                          | Force quit                                               |
| **Save**                      | `:w`                                           | Save                                                     |
| **Save and Exit**             | `:wq`                                          | Save and quit                                            |
| **Modes**                     | `Shift`                                        | Navigate                                                 |
|                               | `i`                                            | Insert mode before the cursor                            |
|                               | `a`                                            | Insert mode after the cursor                             |
|                               | `Shift + A` (`A`)                              | Insert at the end of the line                            |
|                               | `esc esc`                                      | Normal mode                                              |
| **Navigation**                | `gd`                                           | Go to definition of a constant                           |
|                               | `gf`                                           | Open file with function definition                       |
|                               | `Ctrl + o`                                     | Go to previous location                                  |
|                               | `Ctrl + i`                                     | Go forward to next location                              |
| **Delete**                    | `dw`                                           | Delete word                                              |
|                               | `d$`                                           | Delete to end of line                                    |
|                               | `d6w`                                          | Delete 6 words                                           |
|                               | `dd`                                           | Delete line                                              |
|                               | `6dd`                                          | Delete 6 lines                                           |
| **Paste**                     |` p`                                            | Paste after cursor                                       |
|                               | `Shift + p`                                    | Paste before cursor                                      |
| **Undo/Redo**                 | `u`                                            | Undo                                                     |
|                               | `Ctrl + r`                                     | Redo                                                     |
| **Movement Keys**             | `hjkl`                                         | Move (also arrow keys)                                   |
|                               | `w`                                            | Move forward to start of next word                       |
|                               | `e`                                            | Move forward to end of next word                         |
|                               | `b`                                            | Move back to start of previous word                      |
| **Delete Characters**         | `x`                                            | Delete character                                         |
| **Multiplied Movement**       | `6e`                                           | Move to end of 6th word ahead                            |
| **File Navigation**           | `gg`                                           | Go to start of file                                      |
|                               | `G`                                            | Go to end of file                                        |
|                               | `16G`                                          | Go to line 16                                            |
| **Search**                    | `/`                                            | Search forward                                           |
|                               | `?`                                            | Search backward                                          |
|                               | `n`                                            | Next occurrence                                          |
|                               | `N`                                            | Previous occurrence                                      |
| **Parentheses Navigation**    | `%`                                            | Go to matching parenthesis                               |
| **Line Navigation**           | `0`                                            | Go to start of line                                      |
|                               | `$`                                            | Go to end of line                                        |
| **Replace**                   | `:s/the/de`                                    | Replace first occurrence in line                         |
|                               | `:s/the/de/g`                                  | Replace all occurrences in line                          |
|                               | `:%s/numeros/unoAlCinco/g`                     | Replace all occurrences in file                          |
|                               | `:%s/numeros/unoAlCinco/gc`                    | Replace all occurrences with confirmation                |
| **Insert New Line**           | `o`                                            | New line below + insert mode                             |
|                               | `O` (Shift + o)                                | New line above + insert mode                             |
| **Copy and Paste**            | `v`                                            | Visual mode                                              |
|                               | `y`                                            | Yank (copy)                                              |
|                               | `p`                                            | Paste after cursor                                       |
|                               | `P` (Shift + p)                                | Paste before cursor                                      |
| **Clipboard**                 | `"+y`                                          | Yank to clipboard                                        |
|                               | `"+p`                                          | Paste from clipboard                                     |


| **Configuration examples**    |                                                |                                                                                                  |
|-------------------------------|------------------------------------------------|----------------------------------------------------------|
| **file**                      | `~/.vimrc`                                     | Configuration file                                       |
| **Plugin Installation**       | `curl -fLo ~/.vim/autoload/plug.vim --create-dirs \ <url>` | Install vim-plug                             |
|                               | `call plug#begin('~/.vim/plugged')`... `call plug#end()`   | Clause to configure manage plugings          |
|                               | `:PlugIntall`                                  | Command to install pluggings                             |
|                               | `Plug 'easymotion/vim-easymotion'`             | Install Easy moting                                      |
|                               | `Plug 'scrooloose/nerdtree'`                   | Install Nerd Tree plugin                                 |
|                               | `Plug 'christoomey/vim-tmux-navigator'`        | Install GVim Tmux Navigator plugin                       |
|   **Custom Shortcuts**        | `nmap <Leader>nt :NERDTreeFind<CR>`            | Map Nerd Tree                                            |
|                               | `nmap <Leader>s <Plug>(easymotion-s2)`         | Map Easy Motion                                          |
|                               | `nmap <Leader>q :q<CR>`                        | Map quit to shortcut (Not applied)                       |
|                               | `nmap <Leader>w :w<CR>`                        | Map save to shortcut (Not applied)                       |
