# Conway Family Farms — website

Static site for Conway Family Farms (pasture-raised eggs, whole & half hog shares,
raw honey), south of Molalla, Oregon. Hosted on GitHub Pages.

**Preview:** https://conwayfamilyfarms.github.io/conway-family-farms/

## Editing

Pages are assembled from shared header/footer partials in `build.py`:

    python3 build.py   # regenerates the *.html files at the repo root

Edit page bodies / shared header / footer in `build.py`, re-run it, commit both
`build.py` and the regenerated HTML.

## Family of sites

- CFF Genetics (live animals & show pigs): https://conwayfamilyfarms.github.io/cff-genetics/ (planned)
- CFFOS (farm software): https://conwayfamilyfarms.github.io/CFF-os/

## Not yet connected (preview state)

- Forms point at a placeholder Formspree endpoint (`FORM_ENDPOINT` in build.py)
  and are intercepted by `assets/js/main.js` with an honest "not connected" note.
- Buy/Reserve buttons route to the Contact page — Stripe payment links come at
  the commerce hookup step, after the farm's Stripe account is set up.
