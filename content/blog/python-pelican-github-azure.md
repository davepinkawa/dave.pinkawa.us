Title: Python-Generated Static Site into Azure Blob Storage Static Sites via GitHub Actions
Date: 2020-12-16 12:00
Category: Blog
Tags: tech
Slug: python-pelican-github-actions-azure-static-site
Authors: Dave Pinkawa

## Starting the Project

So I bought this new domain name with the intent of having a personal blog, and didn't get around to it until just now. 

I've been meaning to put more Python to use, while also exploring some new tools around the development pipeline platforms. Luckily I've got a standing subscription with Microsoft Azure for other projects I've done in the past, and GitHub has been my source control tool of choice for quite a while now. It was well overdue to combine each of these into my long-standing blog project.

The first thing I looked up was static site generators. I found quite a few, but wanted to focus on ones that were adjacent to languages I've enjoyed using or have been wanting to dive into more.

## Picking Tools 

Some of the static site generators and their respective languages that I looked at:

* Jekyll - Written in Ruby
* Hugo - Written in Go
* Gatsby - Written in React
* Pelican - Written in Python
* Nikola - Written in Python

Unfortunately there's no PowerShell based static site generator, but some people have taken a stab at .Net based ones that could be PowerShell-friendly. 

Because of this, I decided to choose between Pelican or Nikola due to my Python familiarity, and ultimately landed on Pelican for its better-feeling simplicity. I don't think there's a wrong choice with any of these, just personal preference. I was also able to find a community built theme to use with Pelican quite easily, making the time to setup much shorter.

With Pelican chosen, I tinkered around with their quickstart tutorials and was off to the races pretty quickly with local development. Messing with settings in the `pelicanconf.py` file, importing themes with `pelican-themes`, and just getting a general feel for how these files get generated when running `pelican content`. 

Next up was where to host this website, and what were some of my requirements. You won't be surprised to hear that literally every cloud-providing vendor has some form of static site hosting nowadays, so the field of choices was pretty wide.

* GitHub Pages
* AWS S3
* BitBucket
* Azure Blob Storage

I'm certain there are many more out there, but wanting to focus my search to tools I want to work with brought me to Azure Blob Storage based static site hosting. This is a preview feature in Azure as they play catch-up to some of the AWS features available (And the same can be said vice-versa for other features), but it was a fun revisit for me.

My requirements for the site were:

* HTTPS enabled/enforced traffic
* Ability to self-host larger image files for photography
* Custom domain name

The main reason I decided against GitHub pages was the file size limitations for a repository. I would not be able to upload photography images for very long without hitting the limit, and if I'm going to store them in Azure to just be loaded into a GitHub Pages site, I may as well learn how to proceed forward with Azure Blob Storage for all of it.

To get the custom domain and HTTPS enabled did require some configuration of the Azure CDN service. The documentation around creating the CDN association with the Static Site feature is pretty straight forward, and to enforce HTTPS traffic only, you simply create a rule-set in the CDN that redirects all HTTP traffic automatically.

This is where I could finally begin testing the site on an externally hosted location. I manually uploaded via Azure Storage Explorer my `output` folder that Pelican generates, to the static site `$web` container. 

## Automating It All

The idea of having to manually upload these `output` files with every new blog post or page was next. I did _not_ want to manually adjust these things every time.

GitHub Actions was my next tool to jump in feet first. This leverages the files in `.github/workflows` which is `pelican.yml` in my repository here: [https://github.com/davepinkawa/dave.pinkawa.us](https://github.com/davepinkawa/dave.pinkawa.us). 

GitHub automatically picks up the contents of this `.yml` file, and executes them based on content of your `push` configuration.
```
on:
  push:
    branches:
      - main
```
So every time I push new code to the `main` branch, the rest of that workflow executes. What that means is GitHub automatically spins up a container (presumably in Azure, since it's Microsoft-owned) and executes the steps listed. 

For me, those steps are:

1. Setup a Python environment
2. Install pip packages needed for Pelican to run
3. Use the 'Make' command in combination with the `publishconf.py` file, to generate the Pelican Output
4. Uses the community-built `bacongobbler/azure-blob-storage-upload@v1.1.1` to upload the `output` folder to my Azure Blob Storage container `$web` which is the static site location

The coolest part I discovered through this GitHub creation process, is the built-in secrets management that GitHub provides. So in the workflow .yml file, I can input a variable that protects this secret information when the Actions run. Without this, I wouldn't be able to share my blobs source code so openly!

So here's what our final project looks like going forward.

* Clone repository to my computer
* Create new post in `content` folder
* Push to GitHub `main` branch
* This triggers the GitHub action to automatically run
* The Action workflow spins up Pelican, generates the new site, and then pushes to Azure Blob Storage
* Within a few minutes the Azure CDN cache picks up the storage update, and the site is updated!

Well that was a lot, and it's kind of just a high-level overview of it all, but this was a super fun project. 

I promise most of this blog won't be tech-focused, but there will be a good portion as I play around and learn new things. 

Hint hint, Play-Teach-Learn will probably be my next post. This is my personal routine to take on new projects and turn them into long-term learning opportunities that stick with me while also helping others!

-Dave