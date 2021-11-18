# scikit-image.org webpage

## Deploying

*These instructions are now executed automatically every time a new commit
is made to the main branch.  They're provided here in case a manual deploy is needed:*

To build:

```
make gh-pages
```

To upload:

```
cd gh-pages
git push origin master
```

where ``origin`` is
``git@github.com:scikit-image/scikit-image.github.com.git``.
