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

   <script type="text/javascript">
     insert_gallery();
   </script>

   <div class="sideline">

``scikits-image`` is a collection of algorithms for image processing.  It is
available `free of charge and free of restriction </docs/dev/license.html>`__.
We pride ourselves on high-quality, peer-reviewed code, written by an active
`community of volunteers
<https://www.ohloh.net/p/scikits-image/contributors>`__.

.. raw:: html

   </div>
   <br/>

~~~~~~~~~~~
Quick Start
~~~~~~~~~~~

Getting started is easy. For example, if you want to open an image, calculate
a threshold (using Otsu's method), and threshold the image, you just do the
following::

   from skimage import io
   import skimage.filter as imfilt

   image = io.imread('some_image.jpg')
   thresh = imfilt.threshold_otsu(image)
   binary = image > thresh

And ``scikits-image`` uses normal `numpy
<http://docs.scipy.org/doc/numpy/user/whatisnumpy.html>`__ arrays so you can
easily combine this with your favorite scientific tools::

   import matplotlib.pyplot as plt
   plt.imshow(binary)

Have a look at our `gallery </docs/dev/auto_examples>`__ for more examples. Not
all algorithms have examples in the gallery, so check out the `API reference
</docs/dev/api/api.html>`__ for a more complete list.


.. raw:: html

   <div style="clear: left;"></div>

~~~~~~~~~~~~~
Announcements
~~~~~~~~~~~~~

- **SciPy India Sprints** 08/12/2011

- **Release!** Version 0.4 03/12/2011

- **Release!** Version 0.3 10/10/2011

- **Release Sprints** Stanford campus (16 September), online (18 September),
  online (24 September) 2011

- **EuroSciPy Sprint:** at ENS Paris, 29 September 2011

~~~~~~~~~~
Developers
~~~~~~~~~~

 - `Pull requests
   <https://github.com/scikits-image/scikits-image/pulls>`__
 - `Bug reports <https://github.com/scikits-image/scikits-image/issues>`__
 - `Ohloh summary <http://ohloh.net/p/scikits-image>`__
