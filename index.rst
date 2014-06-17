.. meta::
   :google-site-verification: WiJmSOQVA_wT4Zdi1rt3iWNN_EZTcjV6d5GrLHpKVZc

.. title:: scikit-image: Image processing in Python

.. container:: well hero row-fluid summary-box

   .. raw:: html

      <div class="gallery-random">
        <script src="http://scikit-image.org/docs/dev/_static/random.js"></script>
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

      <a class="btn btn-warning clearfix" href="/download">
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
        io.show()

   .. container:: well span6

      .. image:: _static/coins-small.png
         :class: coins-sample span6

      .. image:: _static/sobel-coins-small.png
         :class: coins-sample span6

.. container:: well hero row-fluid summary-box citation

    .. raw:: html

       <b>If you find this project useful, please cite:</b>
       <br/><br/>
       Stéfan van der Walt, Johannes L. Schönberger, Juan Nunez-Inglesias,
       François Boulogne, Joshua D. Warner, Neil Yager, Emmanuelle Gouillart,
       Tony Yu and the scikit-image contributors. <b>scikit-image: Image
       processing in Python</b>. PeerJ PrePrints 2:e336v2 (2012)

       <a href="http://dx.doi.org/10.7287/peerj.preprints.336v2">
       http://dx.doi.org/10.7287/peerj.preprints.336v2
       </a>

Announcements
-------------

- Pre-print of the scikit-image paper: `https://peerj.com/preprints/336/ <https://peerj.com/preprints/336/>`_
- **Release!** Version 0.9.0 19/10/2013
- **Release!** Version 0.8.0 04/03/2013
- **Release!** Version 0.7.0 30/09/2012
- **EuroSciPy Sprint**, Belgium, August 2012
- **SciPy 2012 Sprint**, Austin, July 2012


Developers
----------

- `Pull requests <https://github.com/scikit-image/scikit-image/pulls>`__
- `Bug reports <https://github.com/scikit-image/scikit-image/issues>`__
- `Ohloh summary <http://ohloh.net/p/scikit-image>`__
