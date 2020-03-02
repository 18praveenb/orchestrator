# Website structure

The Github repository has several folders:

- `docs` is where the website output is. Don't edit these files -- they are overwritten whenever the website is built.
   However, you will need to commit them to Github in order for website changes to show up.
- `make-size.zsh` builds the website.
- `pandoc-site` contains the actual website source.
    - `make.zsh` contains the build logic for the website.
    - `temp` contains files that are overwritten on each build -- don't edit/commit these.
    - `t0.html` and `t1.html` are Pandoc's default template split in two so that the link bar can be added to the website.
    - `sources` is where new pages can be added.

To create a new page, create a file `page_name.md` in `pandoc-site/sources`.

It's [Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown)
which is also used in [GitHub readmes](https://guides.github.com/features/mastering-markdown/)
and [Jupyter notebook text cells](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html).[^1]

Add math with `$` (e.g. `$x^3$` becomes $x^3$) and headings with #. You can also add inline HTML.

Add images with `[caption](image-url){.invert}`. The caption is optional. The `invert` is also optional; it makes the image colors flip when the website is in dark mode.

To add local images or Juypter notebooks for download, add them to `resources` then reference then with a link to `./resources/file-name.extension`.

To link to other pages, use `[link-name](page-name.html)`.
Note that even though pages are `.md` files, in the website they will be `.html`, so that's what should be used in the link.

If a page is named with a leading underscore (e.g. `_mypage.md`), then it won't show up in the navigation bar, but the output file will be just `mypage.html`.
This can be useful for creating subpages that are only accessible from another page.
Note that the link would still be `./mypage.html`.

[^1]: Although they all have slightly different syntax for advanced features
