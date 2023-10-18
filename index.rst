.. meta::
   :google-site-verification: WiJmSOQVA_wT4Zdi1rt3iWNN_EZTcjV6d5GrLHpKVZc

.. title:: scikit-image: Image processing in Python

.. container:: well hero row-fluid summary-box

   .. raw:: html

      <div class="gallery-random">
        <script src="https://scikit-image.org/docs/dev/_static/random.js"></script>
        <script type="text/javascript">
          insert_gallery();
        </script>
      </div>

      <h2>Image processing in Python</h2>

   *scikit-image* is a collection of algorithms for image processing.  It
   is available `free of charge and free of restriction
   </docs/dev/license.html>`__.  We pride ourselves on high-quality,
   peer-reviewed code, written by an active `community of volunteers
   <https://www.openhub.net/p/scikit-image/contributors>`__.

   .. raw:: html

      <a class="btn btn-warning clearfix" href="/docs/stable/install.html">
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

       <a href="https://doi.org/10.7717/peerj.453">
       https://doi.org/10.7717/peerj.453
       </a>


News
----

- **Release!** `Version 0.22.0 <https://scikit-image.org/docs/stable/release_notes/release_0.22.html>`__ 2023-10-03
- **Release!** `Version 0.21.0 <https://scikit-image.org/docs/stable/release_notes/release_0.21.html>`__ 2023-06-02
- **Release!** `Version 0.20.0 <https://scikit-image.org/docs/0.20.x/release_notes.html>`__ 2023-02-28
- As part of CZI's 5th EOSS grant cycle, scikit-image received funding to
  `create a typed, discoverable, and extensible API
  <https://chanzuckerberg.com/eoss/proposals/from-library-to-protocol-scikit-image-as-an-api-reference/>`__! 2022-11-30

Getting Started
---------------

Filtering an image with ``scikit-image`` is easy!  For more examples, please
visit our `gallery </docs/dev/auto_examples>`__.

.. container:: row-fluid

   .. container:: span6

      ::

        import skimage as ski

        image = ski.data.coins()
        # ... or any other NumPy array!
        edges = ski.filters.sobel(image)
        ski.io.imshow(edges)
        ski.io.show()

   .. container:: well span6

      .. image:: _static/coins-small.png
         :class: coins-sample span6

      .. image:: _static/sobel-coins-small.png
         :class: coins-sample span6

You can read more in our `user guide </docs/stable/user_guide>`__.
For an introduction to image processing using scikit-image, see
`this lesson <https://datacarpentry.org/image-processing/>`__ by Data Carpentry.

.. include:: team.rst
