.. meta::
   :google-site-verification: WiJmSOQVA_wT4Zdi1rt3iWNN_EZTcjV6d5GrLHpKVZc

.. title:: scikit-image: Image processing in Python

.. container:: well hero row-fluid summary-box

   .. raw:: html

      <div class="gallery-random">
        <script src="http://skimage.org/docs/dev/_static/random.js"></script>
        <script type="text/javascript">
          insert_gallery();
        </script>
      </div>

      <h2>Image processing in Python</h2>

   *scikit-image* is a collection of algorithms for image processing.  It
   is available `free of charge and free of restriction
   </docs/dev/license.html>`__.  We pride ourselves on high-quality,
   peer-reviewed code, written by an active `community of volunteers
   <https://www.ohloh.net/p/scikit-image/contributors>`__.

   .. raw:: html

      <a class="btn btn-warning" href="/download">
      <i class="icon-download icon-white"></i>Download</a>


Getting Started
---------------

Filtering an image with ``scikit-image`` is easy!  For more examples, please
visit our `gallery </docs/dev/auto_examples>`__.

.. container:: row-fluid

   .. container:: span6

      ::

        from skimage import data, io, filter

        image = data.coins() # or any NumPy array!
        edges = filter.sobel(image)
        io.imshow(edges)

   .. container:: well span6

      .. image:: _static/coins-small.png
         :class: coins-sample span6

      .. image:: _static/sobel-coins-small.png
         :class: coins-sample span6


Announcements
-------------

- **Release!** Version 0.7.0 30/09/2012
- **EuroSciPy Sprint**, Belgium, August 2012
- **SciPy 2012 Sprint**, Austin, July 2012
- **Release!** Version 0.6 24/06/2012


Developers
----------

- `Pull requests <https://github.com/scikit-image/scikit-image/pulls>`__
- `Bug reports <https://github.com/scikit-image/scikit-image/issues>`__
- `Ohloh summary <http://ohloh.net/p/scikit-image>`__
