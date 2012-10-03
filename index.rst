.. meta::
   :google-site-verification: WiJmSOQVA_wT4Zdi1rt3iWNN_EZTcjV6d5GrLHpKVZc

.. title::
    scikits-image: Image processing in Python

Getting Started
---------------

Filtering an image with ``scikits-image`` is easy!

.. raw:: html

   <div class="row-fluid">
        <div class="span6">

::

   from skimage import data, io, filter

   image = data.coins() # or any NumPy array!
   edges = filter.sobel(image)
   io.imshow(edges)

For more examples, please visit our `gallery </docs/dev/auto_examples>`__.

.. raw:: html

        </div>
        <div class="well span3 coins-sample">
            <img src="_static/coins-small.png">
        </div>
        <div class="well span3 coins-sample">
            <img src="_static/sobel-coins-small.png">
        </div>
    </div>


Announcements
-------------

- **Release!** Version 0.7.0 30/09/2012
- **EuroSciPy Sprint**, Belgium, August 2012
- **SciPy 2012 Sprint**, Austin, July 2012
- **Release!** Version 0.6 24/06/2012


Developers
----------

- `Pull requests <https://github.com/scikits-image/scikits-image/pulls>`__
- `Bug reports <https://github.com/scikits-image/scikits-image/issues>`__
- `Ohloh summary <http://ohloh.net/p/scikits-image>`__
