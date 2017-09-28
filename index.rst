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


.. container:: well hero row-fluid summary-box citation

    .. raw:: html

       <b>If you find this project useful, please cite:</b>

       <span style="float: right;">
         [<a href="_static/skimage.bib">BiBTeX</a>]
       </span>

       <br/><br/>

       Stéfan van der Walt, Johannes L. Schönberger, Juan Nunez-Iglesias,
       François Boulogne, Joshua D. Warner, Neil Yager, Emmanuelle Gouillart,
       Tony Yu and the scikit-image contributors. <b>scikit-image: Image
       processing in Python</b>. PeerJ 2:e453 (2014)

       <a href="http://dx.doi.org/10.7717/peerj.453">
       http://dx.doi.org/10.7717/peerj.453
       </a>


News
----

- **Release!** Version 0.13.1 2017-09-28
- **Sprint!** SciPy2017, Austin, 10–6 July 2017
- **Release!** Version 0.13 2017-03-29
- **Release!** Version 0.12 2016-03-06
- **Release!** Version 0.11 2015-03-04

Getting Started
---------------

Filtering an image with ``scikit-image`` is easy!  For more examples, please
visit our `gallery </docs/dev/auto_examples>`__.

.. container:: row-fluid

   .. container:: span6

      ::

        from skimage import data, io, filters

        image = data.coins()
        # ... or any other NumPy array!
        edges = filters.sobel(image)
        io.imshow(edges)
        io.show()

   .. container:: well span6

      .. image:: _static/coins-small.png
         :class: coins-sample span6

      .. image:: _static/sobel-coins-small.png
         :class: coins-sample span6

You can read more in our `user guide </docs/dev/user_guide>`__. 


Developers
----------

- `Pull requests <https://github.com/scikit-image/scikit-image/pulls>`__
- `Bug reports <https://github.com/scikit-image/scikit-image/issues>`__
- `Ohloh summary <http://ohloh.net/p/scikit-image>`__
