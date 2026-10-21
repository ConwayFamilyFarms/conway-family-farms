#!/usr/bin/env python3
"""Assemble the Conway Family Farms static site from shared header/footer
partials + per-page bodies. Run: python3 build.py  -> writes *.html at repo root."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

GENETICS_URL = "https://conwayfamilyfarms.github.io/cff-genetics/"  # PROVISIONAL: Genetics site not built yet
CFFOS_URL = "https://conwayfamilyfarms.github.io/CFF-os/"
FB_URL = "https://www.facebook.com/conwayfamilyfarms"   # placeholder handle — confirm before launch
IG_URL = "https://www.instagram.com/conwayfamilyfarms"  # placeholder handle — confirm before launch
FORM_ENDPOINT = "https://formspree.io/f/PLACEHOLDER"    # placeholder — swap at commerce hookup

NAV = [
    ("shop.html", "Shop"),
    ("hog-shares.html", "Hog Shares"),
    ("our-farm.html", "Our Farm"),
    ("for-buyers.html", "For Buyers"),
    ("farm-stand.html", "Visit"),
    ("contact.html", "Contact"),
]

def header(active):
    items = "\n".join(
        '          <li><a href="%s"%s>%s</a></li>' % (
            href, ' aria-current="page"' if href == active else "", label)
        for href, label in NAV)
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%%TITLE%%</title>
<meta name="description" content="%%DESC%%">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&family=Nunito+Sans:wght@400;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>

<div class="family-bar">
  <div class="wrap">
    <span>One farm family, three doors:</span>
    <a href="index.html" aria-current="true">Conway Family Farms</a>
    <a href="__GENETICS__">CFF Genetics — live animals &amp; show pigs</a>
    <a href="__CFFOS__">CFFOS — the farm software</a>
  </div>
</div>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Conway Family Farms — home">
      <img src="assets/img/logo.png" alt="Conway Family Farms oval logo">
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="main-nav">Menu</button>
    <nav class="main-nav" id="main-nav" aria-label="Main">
      <ul>
__ITEMS__
      </ul>
    </nav>
  </div>
</header>
<main id="main">
""".replace("__ITEMS__", items).replace("__GENETICS__", GENETICS_URL).replace("__CFFOS__", CFFOS_URL)

FOOTER = """
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img class="logo" src="assets/img/logo.png" alt="Conway Family Farms oval logo">
        <p>Pasture-raised eggs, pork, and honey from a family farm on 13 acres south of Molalla, Oregon. Regenerative and no-till since 2023.</p>
      </div>
      <div>
        <h3>Visit</h3>
        <ul>
          <li><a href="shop.html">Shop the Farm</a></li>
          <li><a href="hog-shares.html">Whole &amp; Half Hog Shares</a></li>
          <li><a href="farm-stand.html">Farm Stand &amp; Visit</a></li>
          <li><a href="for-buyers.html">For Buyers (Wholesale)</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h3>Our Family of Farms</h3>
        <ul>
          <li><a href="__GENETICS__">CFF Genetics — show pigs &amp; live animals</a></li>
          <li><a href="__CFFOS__">CFFOS — farm management software</a></li>
          <li><a href="__FB__">Facebook</a></li>
          <li><a href="__IG__">Instagram</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-small">
      &copy; <span id="year">2026</span> Conway Family Farms &middot; South of Molalla, Oregon &middot; Est. 2020
      &middot; <a href="index.html">Conway Family Farms</a> &middot; <a href="__GENETICS__">CFF Genetics</a> &middot; <a href="__CFFOS__">CFFOS</a>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
""".replace("__GENETICS__", GENETICS_URL).replace("__CFFOS__", CFFOS_URL).replace("__FB__", FB_URL).replace("__IG__", IG_URL)

PAGES = {}

# ---------------------------------------------------------------- HOME
PAGES["index.html"] = dict(
    title="Conway Family Farms — Fresh Eggs & Pasture-Raised Pork | Molalla, Oregon",
    desc="Pasture-raised eggs, whole & half hog shares, and raw honey from a regenerative family farm south of Molalla, Oregon.",
    active="index.html",
    body="""
<section class="hero">
  <img src="assets/img/hero.jpg" alt="Pastured poultry house on green pasture under a wide sky">
  <div class="hero-text">
    <div class="wrap">
      <h1>Conway Family Farms</h1>
      <p class="tagline">Fresh Eggs &amp; Pasture-Raised Pork, Raised Right Here</p>
      <p class="sub">A family farm on 13 acres south of Molalla, Oregon — regenerative, no-till since 2023, and run by the family that lives here.</p>
      <div class="btn-row">
        <a class="btn btn-sage" href="shop.html">Visit the Shop</a>
        <a class="btn btn-cream" href="hog-shares.html">How Hog Shares Work</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <h2>Raised right here, on pasture</h2>
      <p>Our hens follow fresh grass in mobile coops, our pigs root and graze the way pigs are meant to, and our bees work the hedgerows. No shortcuts, no feedlot — just animals on grass, raised by our family.</p>
      <p>Everything we sell is raised or made on this farm, and the way we sell it is simple on purpose: eggs by the dozen, honey by the jar, and pork by the whole or half animal — the way farm families have always bought it.</p>
      <a class="btn btn-outline" href="our-farm.html">Our Story</a>
    </div>
    <img src="assets/img/hens.jpg" alt="A red laying hen looking at the camera" loading="lazy">
  </div>
</section>

<section class="section shop-banner">
  <div class="wrap split">
    <div>
      <h2>Shop the Farm</h2>
      <p class="lede">Eggs by the dozen from our pastured hens. Whole and half hog shares to fill your freezer. Raw honey from our own hives. Head to the shop to see what&rsquo;s available and how to get it.</p>
      <a class="btn btn-sage" href="shop.html">Visit the Shop</a>
    </div>
    <div class="thumbs" aria-hidden="true">
      <img src="assets/img/eggs.jpg" alt="" loading="lazy">
      <img src="assets/img/honey.jpg" alt="" loading="lazy">
      <img src="assets/img/pigs.jpg" alt="" loading="lazy">
      <img src="assets/img/bees.jpg" alt="" loading="lazy">
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="barn-sign">
      <h2>Whole &amp; Half Hog Shares</h2>
      <p>Reserve a whole or half hog for your freezer — pasture-raised here, processed locally in Oregon. A deposit holds your share.</p>
      <a class="btn btn-cream" href="hog-shares.html">Reserve Your Share</a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap grid grid-2">
    <article class="card">
      <img src="assets/img/stand.jpg" alt="A farm stand table piled with fresh vegetables" loading="lazy">
      <div class="card-body">
        <h3>Visit the Farm Stand — South of Molalla, Oregon</h3>
        <p>Our roadside stand is open around the clock, stocked as the harvest comes in — seasonal produce, eggs, and honey, freshest first. Stop by any time and say hello to the flock.</p>
        <a class="btn btn-sage" href="farm-stand.html">Plan Your Visit</a>
      </div>
    </article>
    <article class="card">
      <img src="assets/img/pigs.jpg" alt="Young pigs grazing on green pasture" loading="lazy">
      <div class="card-body">
        <h3>For Buyers</h3>
        <p>We supply whole animals and feeder stock for butchers, chefs, and restaurants. Partner with us for quality pasture-raised pork on a consistent basis.</p>
        <a class="btn btn-sage" href="for-buyers.html">Contact for Wholesale</a>
      </div>
    </article>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>One farm family, three doors</h2>
    <p class="lede">Looking for something else we do? You&rsquo;re one click away.</p>
    <div class="grid grid-2">
      <article class="card">
        <div class="card-body">
          <h3>CFF Genetics</h3>
          <p>Live animals live over there — show pigs, weaner pigs, and breeding stock from our genetics program.</p>
          <a class="btn btn-outline" href="__GENETICS__">Visit CFF Genetics</a>
        </div>
      </article>
      <article class="card">
        <div class="card-body">
          <h3>CFFOS</h3>
          <p>The software that runs this farm — animal records, Prop 12 movement tracking, and farm management built by a farmer.</p>
          <a class="btn btn-outline" href="__CFFOS__">Visit CFFOS</a>
        </div>
      </article>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- SHOP
PAGES["shop.html"] = dict(
    title="Shop — Conway Family Farms",
    desc="Whole & half hog shares, pasture-raised eggs by the dozen, and raw honey from Conway Family Farms, south of Molalla, Oregon.",
    active="shop.html",
    body="""
<section class="page-hero">
  <div class="wrap">
    <h1>Shop the Farm</h1>
    <p>Everything here is raised or made on this farm. We sell pork the whole-animal way — by the share, not by the cut — so our hogs go from pasture to your freezer without ever sitting in ours.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="barn-sign" style="text-align:left">
      <h2>Whole &amp; Half Hog Shares — Our Main Offer</h2>
      <p style="margin-left:0">Reserve a whole or half hog, raised on pasture here and processed at Mt. Angel Meat. Priced per pound on hanging weight; your deposit is credited to your final invoice, and you choose your own cuts.</p>
      <p style="margin-left:0"><strong>Deposit:</strong> $250 for a whole hog &middot; $150 for a half — holds your share.</p>
      <div class="btn-row">
        <a class="btn btn-cream" href="contact.html">Reserve Your Share</a>
        <a class="btn btn-outline" style="border-color:#f6efdb;color:#f6efdb" href="hog-shares.html">How Shares Work</a>
      </div>
      <p class="note" style="color:#cfd6bd;margin:14px 0 0">Online reservations open soon. Join the share list through the contact page and we&rsquo;ll reach out in order when the next batch opens.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2>The Staples</h2>
    <div class="grid grid-2">
      <article class="card">
        <img src="assets/img/eggs.jpg" alt="Brown eggs in a carton" loading="lazy">
        <div class="card-body">
          <h3>Farm Eggs</h3>
          <p>By the dozen &middot; free-range &middot; pasture-raised. Deep orange yolks from hens that actually go outside.</p>
          <p class="price">$6 / dozen</p>
          <a class="btn btn-sage" href="contact.html">Ask About Eggs</a>
        </div>
      </article>
      <article class="card">
        <img src="assets/img/honey.jpg" alt="A jar of raw honey with a honey dipper" loading="lazy">
        <div class="card-body">
          <h3>Raw Honey</h3>
          <p>8 oz jar &middot; raw &amp; unfiltered, from hives here on the farm. Tastes like the hedgerows it came from.</p>
          <p class="price">$14 / jar</p>
          <a class="btn btn-sage" href="contact.html">Ask About Honey</a>
        </div>
      </article>
    </div>
    <p class="note" style="margin-top:16px">Eggs and honey are picked up at the farm stand — it&rsquo;s roadside and open around the clock; see the <a href="farm-stand.html">Visit page</a>. Seasonal garden goods show up at the stand through the year, first come, first served.</p>
  </div>
</section>

<section class="section alt">
  <div class="wrap split">
    <img src="assets/img/bees.jpg" alt="Beehives on a green hillside" loading="lazy">
    <div>
      <h2>Farm merch is on its way</h2>
      <p>Tote bags, camp mugs, and stickers with the farm brands are in the works. Join the farm list and you&rsquo;ll hear the day they land.</p>
      <a class="btn btn-outline" href="contact.html">Join the Farm List</a>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- HOG SHARES
PAGES["hog-shares.html"] = dict(
    title="Whole & Half Hog Shares — Conway Family Farms",
    desc="How hog shares work at Conway Family Farms: reserve with a deposit, we raise your hog on pasture, processing through Mt. Angel Meat, pickup.",
    active="hog-shares.html",
    body="""
<section class="section" style="padding-bottom:0">
  <div class="wrap">
    <div class="barn-sign">
      <h1 style="color:#fdfaf0">Whole &amp; Half Hog Shares</h1>
      <p>Reserve a whole or half hog for your freezer — pasture-raised, processed locally in Oregon. A deposit holds your share.</p>
      <a class="btn btn-cream" href="contact.html">Join the Share List</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>How it works</h2>
    <ol class="steps">
      <li><h3>Reserve</h3><p>Join the share list and put down a deposit — $250 for a whole hog, $150 for a half. The deposit holds your animal and is credited to your final invoice.</p></li>
      <li><h3>We raise your hog</h3><p>Your hog is raised here on pasture, on our batch calendar, the same way we raise all our pigs.</p></li>
      <li><h3>Butcher date</h3><p>When your batch reaches finish weight, we set the butcher date and let you know your hog&rsquo;s hanging weight.</p></li>
      <li><h3>Processing</h3><p>Your hog is processed at Mt. Angel Meat (Mt. Angel, Oregon). You fill out a cut sheet and choose your cuts — chops, roasts, bacon, ham, sausage, and more.</p></li>
      <li><h3>Pickup</h3><p>You pay the balance to us and the processing to the processor, and pick up your boxed, labeled pork.</p></li>
    </ol>
  </div>
</section>

<section class="section alt">
  <div class="wrap grid grid-2" style="align-items:start">
    <div>
      <h2>Pricing, in plain words</h2>
      <p>Shares are priced <strong>per pound on hanging weight</strong> — the weight of the hog after harvest, before cutting. Your deposit comes off the top of your final invoice. Processing (kill fee and cut &amp; wrap) is paid by you, directly to Mt. Angel Meat, at their current rates.</p>
      <p>Our per-pound price for the next batch is being finalized from our cost records right now. Join the share list and you&rsquo;ll get the price — and first pick of butcher dates — before reservations open to everyone else.</p>
      <h3 style="margin-top:1.2em">What you get</h3>
      <p>A finished whole hog typically hangs at 180–240 lb. After cutting, roughly two-thirds to three-quarters of that lands in your freezer as packaged pork — chops, roasts, ribs, bacon, ham, ground pork, and sausage, cut the way you asked for them. A half share is the same, in half the quantity, from one side of the animal.</p>
    </div>
    <div class="example">
      <h3>Example math — round numbers, not our price</h3>
      <p>So there are no surprises, here&rsquo;s how the bill works on a sample whole hog:</p>
      <table class="spec">
        <tr><th>Hanging weight</th><td>200 lb</td></tr>
        <tr><th>Example price</th><td>$5.00 / lb hanging</td></tr>
        <tr><th>Owed to the farm</th><td>200 &times; $5.00 = $1,000</td></tr>
        <tr><th>Deposit credited</th><td>&minus; $250</td></tr>
        <tr><th>Balance to the farm</th><td>$750, due at the butcher date</td></tr>
        <tr><th>Processing</th><td>Paid by you to Mt. Angel Meat (kill fee + cut &amp; wrap at their current rates)</td></tr>
      </table>
      <p class="note" style="margin-top:12px">The $5.00/lb above is an example to show the math only. Our actual per-pound price is announced to the share list first.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="photo-band">
      <img src="assets/img/pigs.jpg" alt="Young pigs grazing on green pasture" loading="lazy">
      <img src="assets/img/piglet.jpg" alt="A young piglet standing in straw" loading="lazy">
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2>Questions we hear</h2>
    <details><summary>When are the butcher dates?</summary>
      <p>Shares move on our batch calendar, so dates are set per batch. Share-list members hear the dates — and get first claim — as soon as a batch is scheduled.</p></details>
    <details><summary>What if I only want a half?</summary>
      <p>Order a half share — same process, half the pork. Or split a whole hog with a friend or another family; one deposit holds it, and the processor boxes each half to your own cut sheets.</p></details>
    <details><summary>When do I pay?</summary>
      <p>The deposit when you reserve, the balance to the farm at the butcher date, and processing to Mt. Angel Meat when you pick up.</p></details>
    <details><summary>Where do I pick up?</summary>
      <p>At Mt. Angel Meat in Mt. Angel, Oregon — they&rsquo;ll have your boxes labeled and frozen, ready to load.</p></details>
    <details><summary>Do I choose my own cuts?</summary>
      <p>Yes. You&rsquo;ll fill out a cut sheet with the processor — thickness of chops, roast sizes, how much goes to sausage and ground, and how the hams and bacon are cured.</p></details>
    <div class="barn-sign" style="margin-top:26px">
      <h2>Ready to fill a freezer?</h2>
      <p>Join the share list and we&rsquo;ll contact you in order when the next batch opens.</p>
      <a class="btn btn-cream" href="contact.html">Join the Share List</a>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- OUR FARM
PAGES["our-farm.html"] = dict(
    title="Our Farm — Conway Family Farms",
    desc="The story of Conway Family Farms: 13 acres south of Molalla toward Silverton, regenerative and no-till since 2023 — eggs, pigs, garden, and bees.",
    active="our-farm.html",
    body="""
<section class="page-hero">
  <div class="wrap">
    <h1>Our Farm</h1>
    <p>Thirteen acres south of Molalla, toward Silverton — a family farm, worked by the family that lives on it.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <h2>Land first, since day one</h2>
      <p>Conway Family Farms started in 2020 with a simple order of priorities: take care of the ground, take care of the animals, and the food takes care of itself. We&rsquo;ve farmed regeneratively and no-till since 2023 — no plowing up the soil life we depend on, and every enterprise on the place has to earn its keep without costing the pasture.</p>
      <p>That&rsquo;s also why we exited cattle: pasture health comes first here, ahead of any single enterprise. When the land said the herd was too much for it, we listened.</p>
    </div>
    <img src="assets/img/hens-coop.jpg" alt="Hens coming down the ramp of their mobile coop" loading="lazy">
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>What we raise</h2>
    <div class="grid grid-2">
      <article class="card">
        <img src="assets/img/hens.jpg" alt="A red laying hen looking at the camera" loading="lazy">
        <div class="card-body"><h3>Pastured eggs</h3>
        <p>A laying flock that lives on grass in mobile coops, moved to fresh ground — the eggs are the farm&rsquo;s daily bread.</p></div>
      </article>
      <article class="card">
        <img src="assets/img/pigs.jpg" alt="Young pigs grazing on green pasture" loading="lazy">
        <div class="card-body"><h3>Pasture-raised pigs</h3>
        <p>Pigs on pasture, raised in batches matched to the seasons — sold as whole and half shares, weaners, and show pigs through <a href="__GENETICS__">CFF Genetics</a>.</p></div>
      </article>
      <article class="card">
        <img src="assets/img/garden.jpg" alt="A scoop of rich garden soil" loading="lazy">
        <div class="card-body"><h3>The garden</h3>
        <p>No-till beds feeding the farm stand through the season — what&rsquo;s ripe is what&rsquo;s on the table.</p></div>
      </article>
      <article class="card">
        <img src="assets/img/bees.jpg" alt="Beehives on a green hillside" loading="lazy">
        <div class="card-body"><h3>Bees &amp; honey</h3>
        <p>Hives along the hedgerows; once they&rsquo;re established, the bees mostly run themselves and give us raw honey to share.</p></div>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <img src="assets/img/eggs-hands.jpg" alt="Hands holding a bowl of fresh brown eggs" loading="lazy">
    <div>
      <h2>Working with the land, on paper too</h2>
      <p>Our pasture work isn&rsquo;t just habit — we run USDA/NRCS contract projects on this farm covering pasture management and rotation, high tunnels, and hedgerows, the same practices we&rsquo;d tell any farm to build on. And every animal movement on the place is recorded for Prop 12 compliance, using <a href="__CFFOS__">CFFOS</a> — the farm software built right here.</p>
      <div class="btn-row">
        <a class="btn btn-sage" href="shop.html">Shop the Farm</a>
        <a class="btn btn-outline" href="for-buyers.html">For Buyers</a>
      </div>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- FARM STAND
PAGES["farm-stand.html"] = dict(
    title="Visit the Farm Stand — Conway Family Farms",
    desc="Visit the Conway Family Farms stand south of Molalla, Oregon — eggs, honey, and seasonal produce.",
    active="farm-stand.html",
    body="""
<section class="page-hero">
  <div class="wrap">
    <h1>Visit the Farm Stand</h1>
    <p>South of Molalla, Oregon. Come buy something fresh and say hello to the flock.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <img src="assets/img/stand.jpg" alt="A farm stand table piled with fresh vegetables" loading="lazy">
    <div>
      <h2>Finding us</h2>
      <table class="spec">
        <tr><th>Hours</th><td>Open 24 hours a day, every day — roadside and self-serve</td></tr>
        <tr><th>Where</th><td>South of Molalla, Oregon <span class="placeholder">[street address &amp; directions to be added]</span></td></tr>
        <tr><th>What&rsquo;s here</th><td>Farm eggs, raw honey, and whatever the garden is producing this week</td></tr>
        <tr><th>Payment</th><td>Cash and card welcome</td></tr>
      </table>
      <p style="margin-top:14px">The stand sits at the roadside and never closes — swing by any time and help yourself. We stock it as the harvest comes in, so what&rsquo;s on the table is the freshest thing on the farm right now.</p>
      <p class="note" style="margin-top:14px">Egg customers: the stand is the pickup point for dozens ordered ahead through the <a href="contact.html">contact page</a>.</p>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>What to expect</h2>
    <div class="grid grid-3">
      <article class="card"><div class="card-body"><h3>Seasonal, honestly</h3>
      <p>The stand table changes with the garden. When something&rsquo;s gone, it&rsquo;s gone until the next planting — we don&rsquo;t truck in produce to fill gaps.</p></div></article>
      <article class="card"><div class="card-body"><h3>Eggs &amp; honey, most weeks</h3>
      <p>The staples travel with us: dozens from the pastured flock and jars of raw honey from our own hives.</p></div></article>
      <article class="card"><div class="card-body"><h3>Ask us anything</h3>
        <p>How the animals are raised, when hog shares open, what&rsquo;s planting next — the stand is the easiest place to talk farm. For hog shares specifically, start on the <a href="hog-shares.html">shares page</a>.</p></div></article>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- FOR BUYERS
PAGES["for-buyers.html"] = dict(
    title="For Buyers — Wholesale Pork | Conway Family Farms",
    desc="Wholesale whole animals and feeder stock from Conway Family Farms: Prop 12 certified, pasture-raised, batch availability for butchers and chefs.",
    active="for-buyers.html",
    body="""
<section class="page-hero">
  <div class="wrap">
    <h1>For Buyers</h1>
    <p>For butchers, chefs, and restaurants: what we raise, how we raise it, and when it&rsquo;s available. No form maze — talk to the farmer directly.</p>
  </div>
</section>

<section class="section">
  <div class="wrap grid grid-2" style="align-items:start">
    <div>
      <h2>What we raise, and how</h2>
      <p>Pasture-based, regenerative pork from a 13-acre family farm south of Molalla. Our herd is moving toward Duroc-based genetics specifically for a consistent animal and a consistent product your customers can count on, batch after batch.</p>
      <table class="spec">
        <tr><th>Certification</th><td>Prop 12 certified — every animal movement recorded (we run our own record-keeping software, <a href="__CFFOS__">CFFOS</a>)</td></tr>
        <tr><th>Practices</th><td>Pasture-raised, rotationally managed; regenerative, no-till farm since 2023</td></tr>
        <tr><th>Contract work</th><td>USDA/NRCS projects on pasture management &amp; rotation, high tunnels, and hedgerows</td></tr>
        <tr><th>Processing</th><td>Our own animals are processed through Mt. Angel Meat (Eric), Mt. Angel, Oregon</td></tr>
      </table>
      <h3 style="margin-top:1.4em">Talk to Kris directly</h3>
      <p>Phone: <span class="placeholder">[phone to be added]</span><br>
      Email: <span class="placeholder">[email to be added]</span></p>
      <p class="note">Looking for <strong>live animals</strong> instead — show pigs, weaners, breeding stock? That&rsquo;s <a href="__GENETICS__">CFF Genetics</a>.</p>
    </div>
    <div>
      <h2>Batch availability</h2>
      <table class="spec">
        <tr><th>January / February batch</th><td>Our main farrowing. Weaner pigs sell in March/April; pigs from this batch reach fair age for the county fair season.</td></tr>
        <tr><th>November / December batch</th><td>Starting next year: whole animals for buyers, plus grower/feeder stock held a month or two past weaning.</td></tr>
        <tr><th>Whole animals</th><td>Available by batch — talk to us about weights, finish, and dates, and we&rsquo;ll breed and finish to your spec on our calendar.</td></tr>
      </table>
      <h3 style="margin-top:1.4em">Buyer inquiry</h3>
      <!-- Form endpoint is a placeholder until commerce hookup (see build.py FORM_ENDPOINT). -->
      <form class="f" method="post" action="__FORM__" data-preview>
        <label>Your name <input name="name" required autocomplete="name"></label>
        <label>Business <input name="business" autocomplete="organization"></label>
        <label>Email <input type="email" name="email" required autocomplete="email"></label>
        <label>What are you looking for?
          <select name="interest">
            <option>Whole animals</option>
            <option>Feeder / grower stock</option>
            <option>Weaner pigs</option>
            <option>Something else</option>
          </select></label>
        <label>Details — volume, weights, timing <textarea name="message"></textarea></label>
        <div><button class="btn btn-sage" type="submit">Send Inquiry</button></div>
        <p class="form-note" role="status">Thanks — this preview form isn&rsquo;t connected yet, so nothing was sent. It will deliver straight to the farm&rsquo;s inbox at launch.</p>
      </form>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- CONTACT
PAGES["contact.html"] = dict(
    title="Contact — Conway Family Farms",
    desc="Contact Conway Family Farms — hog shares, eggs and honey, wholesale inquiries, and the farm list.",
    active="contact.html",
    body="""
<section class="page-hero">
  <div class="wrap">
    <h1>Contact the Farm</h1>
    <p>Hog shares, eggs and honey, wholesale, or just a question — this is the one door for all of it.</p>
  </div>
</section>

<section class="section">
  <div class="wrap grid grid-2" style="align-items:start">
    <div>
      <h2>Send a message</h2>
      <!-- Form endpoint is a placeholder until commerce hookup (see build.py FORM_ENDPOINT). -->
      <form class="f" method="post" action="__FORM__" data-preview>
        <label>Your name <input name="name" required autocomplete="name"></label>
        <label>Email <input type="email" name="email" required autocomplete="email"></label>
        <label>Phone (optional) <input type="tel" name="phone" autocomplete="tel"></label>
        <label>I&rsquo;m asking about
          <select name="topic">
            <option>Whole / half hog shares</option>
            <option>Eggs &amp; honey</option>
            <option>Join the farm list</option>
            <option>Wholesale / buyer inquiry</option>
            <option>Live animals (CFF Genetics)</option>
            <option>Something else</option>
          </select></label>
        <label>Message <textarea name="message" required></textarea></label>
        <div><button class="btn btn-sage" type="submit">Send Message</button></div>
        <p class="form-note" role="status">Thanks — this preview form isn&rsquo;t connected yet, so nothing was sent. It will deliver straight to the farm&rsquo;s inbox at launch.</p>
      </form>
      <p class="note" style="margin-top:12px">Asking about live animals — show pigs, weaners, breeding stock? You&rsquo;ll get a faster answer at <a href="__GENETICS__">CFF Genetics</a>.</p>
    </div>
    <div>
      <h2>Other ways to reach us</h2>
      <table class="spec">
        <tr><th>Phone</th><td><span class="placeholder">[phone to be added]</span></td></tr>
        <tr><th>Email</th><td><span class="placeholder">[email to be added]</span></td></tr>
        <tr><th>Farm stand</th><td>South of Molalla, Oregon — roadside stand, open 24 hours a day (<a href="farm-stand.html">visit page</a>)</td></tr>
        <tr><th>Social</th><td><a href="__FB__">Facebook</a> &middot; <a href="__IG__">Instagram</a> — @conwayfamilyfarms</td></tr>
      </table>
      <h3 style="margin-top:1.4em">Join the farm list</h3>
      <p>Share openings, butcher dates, stand season, and litter news go to the list first. Pick &ldquo;Join the farm list&rdquo; in the form and say the word.</p>
      <img src="assets/img/hens-coop.jpg" alt="Hens coming down the ramp of their mobile coop" loading="lazy" style="border-radius:14px;margin-top:10px">
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- assemble
for fname, page in PAGES.items():
    html = header(page["active"]) + page["body"] + FOOTER
    html = html.replace("%%TITLE%%", page["title"]).replace("%%DESC%%", page["desc"])
    html = html.replace("__GENETICS__", GENETICS_URL).replace("__CFFOS__", CFFOS_URL)
    html = html.replace("__FB__", FB_URL).replace("__IG__", IG_URL).replace("__FORM__", FORM_ENDPOINT)
    with open(os.path.join(ROOT, fname), "w") as fh:
        fh.write(html)
    print("wrote", fname, len(html), "bytes")
