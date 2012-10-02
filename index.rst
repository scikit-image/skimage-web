.. meta::
   :google-site-verification: WiJmSOQVA_wT4Zdi1rt3iWNN_EZTcjV6d5GrLHpKVZc

.. raw:: html

   <style type="text/css">
     h1 {
         display: none;
         margin: 0;
         padding: 0;
     }
   </style>

   <script type="text/javascript"
           src="http://scikits-image.org/docs/dev/_static/random.js"></script>

====================================================
scikits-image: An image processing toolbox for SciPy
====================================================

.. raw:: html

    <div class="gallery_random">
        <script type="text/javascript">
            insert_gallery();
        </script>
    </div>

    <div class="sideline">

``scikits-image`` is a collection of algorithms for image processing.  It is
available `free of charge and free of restriction </docs/dev/license.html>`__.
We pride ourselves on high-quality, peer-reviewed code, written by an active
`community of volunteers
<https://www.ohloh.net/p/scikits-image/contributors>`__.

.. raw:: html

   </div>

   <div style="clear: left;"></div>

~~~~~~~~~~~~~~~
Getting Started
~~~~~~~~~~~~~~~

.. raw:: html

   <div style="float: left; width: 45%; padding-right: 5%;">

Filtering an image with ``scikits-image`` is easy!

::

   from skimage import data, io, filter

   image = data.coins() # or any NumPy array!
   edges = filter.sobel(image)
   io.imshow(edges)

For more examples, please visit our `gallery </docs/dev/auto_examples>`__.

.. raw:: html

   </div>

   <div class="gallery_image" style="float: right;">
       <img src="_static/coins_small.png" style="width:150px; float:left; margin-right:10px;" />
       <img src="_static/sobel_coins_small.png" style="width:150px; float:left;"/>
       <div style="clear: left;"></div>
   </div>

   <div style="clear: left;"></div>


~~~~~~~~~~~~~
Announcements
~~~~~~~~~~~~~

- **Release!** Version 0.7.0 30/09/2012
- **EuroSciPy Sprint**, Belgium, August 2012
- **SciPy 2012 Sprint**, Austin, July 2012
- **Release!** Version 0.6 24/06/2012

~~~~~~~~~~
Developers
~~~~~~~~~~

- `Pull requests <https://github.com/scikits-image/scikits-image/pulls>`__
- `Bug reports <https://github.com/scikits-image/scikits-image/issues>`__
- `Ohloh summary <http://ohloh.net/p/scikits-image>`__
