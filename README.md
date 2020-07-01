# README tournament-management-racket

## Preamble

I recently discovered that using Kindle highlights saved me the trouble of typing out quotations from my reading. However, I rapidly got bored of having to take the supplied CSV, reformatting it for my notes and supplying the pandoc citation for each quotation. This solves this problem for me, but it is not elegant, nor does it handle for anything other than the intended use case. 


This is a simple Python 3.8 script, with no additional testing. I created it on Ubuntu 16.04. It uses f-strings, which means it won't work as is for versions prior to 3.6.

## Installation

A simple Python 3.8 script; should run from terminal, within the program directory, with the command `python3.8 quotation_reformatter.py`.

## Usage

Export your notes from your Kindle; they should arrive as a CSV and a PDF to the email address associated with your Amazon account.


Download the CSV and dump it in the input folder.


Open the terminal at the program directory, and run `python3.8 quotation_reformatter.py`.


When prompted supply the details of the pandoc citation, without any of the `[@ ]`, i.e. `imai_gemba_2012`. 


A confirmation message should be printed to the terminal for each quotation processed, and then the a final notification that the program is complete. In the output folder there should now be a file entitled `your_citation_2020.md` for whatever citation you provided, with the quotes, in pandoc indents, with quotation marks around them, and with the appropriate pandoc citation at the end of each one, ready to drop into your notes. 


## NB

**This script does not distinguish between locations and pages.** Pandoc doesn't handle Kindle locations anyway. This is because this script supports my workflow, and while this takes out a lot of the effort, I now process this into my zettelkasten and will manually edit out the bits I don't need. 


**This script does not distinguish between quotations and notes.** I have another method for taking notes when reading as I find the Kindle keyboard resistant to typing. Therefore I haven't handled for separating notes from highlights. 



## Contributing


## License

