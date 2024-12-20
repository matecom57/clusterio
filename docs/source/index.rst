¡Bienvenido a la documentación de Don Clusterio!
===================================

referencia: `wiki <https://github.com/c13inb/c13inb.github.io/wiki/>`_

:doc:`cross`

Home

Ricardo Rios edited this page Mar 13, 2024 · `43 revisions <https://github.com/c13inb/c13inb.github.io/wiki/Home/_history>`_

Bienvenidos a la MRI-lab Wiki!
------------------------------

.. _target to paragraph:

Bienvenido a la wiki del **Laboratorio de Imágenes de Resonancia Magnética**. Esta página contiene el repositorio para la wiki y herramientas de los usuarios del MRI-lab.

    ⭐ No olvides también visitar la `wiki del Lanirem <https://github.com/lanirem/documentation/wiki/XCP-Preprocessing/>`_, donde puedes encontrar aún más información!

    ⚠️ Todo usuario del cluster Don Clusterio debe estar inscrito en la Red Lanirem en el canal `#don_clusterio <https://chat-lanirem.lavis.unam.mx/channel/don_clusterio/>`_. No hacerlo implica la desactivación de la cuenta.

How to use cross-references with Sphinx
=======================================

.. contents:: Table of contents
   :local:
   :backlinks: none
   :depth: 3

Getting started
---------------

.. _My target:

MRILab Wiki
~~~~~~~~~~~

Este wiki intenta facilitar el uso del clúster y las máquinas que lo forman. Cualquier persona puede consultar la wiki desde una computadora con acceso a internet.

Te invitamos a apoyar el desarrollo de esta wiki de las siguientes formas:

    Si deseas complementar o corregir alguna entrada que ya está en la wiki.
    Si aprendes algo nuevo y lo quieres incluir en esta wiki para que los demás podamos aprenderlo también.

Si deseas colaborar en esta wiki es necesario tener una cuenta de github y ser colaborador de este repositorio-wiki. Mas info en este link

For example, one way of creating an explicit target for a section is:

.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         .. _My target:

         Explicit targets
         ~~~~~~~~~~~~~~~~

         Reference `My target`_.

   .. tab:: MyST (Markdown)

      .. code-block:: md

         (My_target)=
         ## Explicit targets

         Reference [](My_target).


You can also add explicit targets before paragraphs (or any other part of a page).

Another example, add a target to a paragraph:

.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         .. _target to paragraph:

         An easy way is just to use the final link of the page/section.
         This works, but it has :ref:`some disadvantages <target to paragraph>`:

   .. tab:: MyST (Markdown)

      .. code-block:: md

         (target_to_paragraph)=

         An easy way is just to use the final link of the page/section.
         This works, but it has [some disadvantages](target_to_paragraph):




For example, an in-line target inside a paragraph:

.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         You can also create _`in-line targets` within an element on your page,
         allowing you to, for example, reference text *within* a paragraph.



Implicit targets
~~~~~~~~~~~~~~~~

You may also reference some objects by name
without explicitly giving them one
by using *implicit targets*.

When you create a section, a footnote, or a citation,
Sphinx will create a target with the title as the name:

.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         For example, to reference the previous section
         you can use `Explicit targets`_.

   .. tab:: MyST (Markdown)

      .. code-block:: md

         For example, to reference the previous section
         you can use [](#explicit-targets).

      .. note::

         This requires setting ``myst_heading_anchors = 2`` in your ``conf.py``,
         see :ref:`myst-parser:syntax/header-anchors`.


Cross-referencing using roles
-----------------------------

All targets seen so far can be referenced only from the same page.
Sphinx provides some roles that allow you to reference any explicit target from any page.

.. note::

   Since Sphinx will make all explicit targets available globally,
   all targets must be unique.

You can see the complete list of cross-referencing roles at :ref:`sphinx:xref-syntax`.
Next, you will explore the most common ones.

The ref role
~~~~~~~~~~~~

The ``ref`` role can be used to reference any explicit targets. For example:

.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         - :ref:`my target`.
         - :ref:`Target to paragraph <target to paragraph>`.
         - :ref:`Target inside a paragraph <in-line targets>`.

   .. tab:: MyST (Markdown)

      .. code-block:: md

         - {ref}`my target`.
         - {ref}`Target to paragraph <target_to_paragraph>`.

That will be rendered as:

- :ref:`my target`.
- :ref:`Target to paragraph <target to paragraph>`.
- :ref:`Target inside a paragraph <in-line targets>`.

The ``ref`` role also allow us to reference code blocks:

.. code-block:: rst

   .. _target to code:

   .. code-block:: python

      # Add the extension
      extensions = [
         'sphinx.ext.autosectionlabel',
      ]

      # Make sure the target is unique
      autosectionlabel_prefix_document = True

We can reference it using ``:ref:`code <target to code>```,
that will be rendered as: :ref:`code <target to code>`.

The doc role
~~~~~~~~~~~~

The ``doc`` role allows us to link to a page instead of just a section.
The target name can be relative to the page where the role exists, or relative
to your documentation's root folder (in both cases, you should omit the extension).

For example, to link to a page in the same directory as this one you can use:

.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         - :doc:`intersphinx`
         - :doc:`/guides/intersphinx`
         - :doc:`Custom title </guides/intersphinx>`

   .. tab:: MyST (Markdown)

      .. code-block:: md

         - {doc}`intersphinx`
         - {doc}`/guides/intersphinx`
         - {doc}`Custom title </guides/intersphinx>`

That will be rendered as:

- :doc:`intersphinx`
- :doc:`/guides/intersphinx`
- :doc:`Custom title </guides/intersphinx>`

.. tip::

   Using paths relative to your documentation root is recommended,
   so you avoid changing the target name if the page is moved.

The numref role
~~~~~~~~~~~~~~~

The ``numref`` role is used to reference **numbered** elements of your documentation.
For example, tables and images.

To activate numbered references, add this to your ``conf.py`` file:

.. code-block:: python

   # Enable numref
   numfig = True

Next, ensure that an object you would like to reference has an explicit target.

For example, you can create a target for the next image:

.. _target to image:

.. figure:: /img/logo.png
   :alt: Logo
   :align: center
   :width: 240px

   Link me!

.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         .. _target to image:

         .. figure:: /img/logo.png
            :alt: Logo
            :align: center
            :width: 240px

            Link me!

   .. tab:: MyST (Markdown)

      .. code-block:: md

         (target_to_image)=

         ```{figure} /img/logo.png
         :alt: Logo
         :align: center
         :width: 240px
         ```

Finally, reference it using ``:numref:`target to image```,
that will be rendered as ``Fig. N``.
Sphinx will enumerate the image automatically.

