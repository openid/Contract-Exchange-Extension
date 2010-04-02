==============================
Sample XML and XML Schema(xsd)
==============================

File
====

- cx.xml 
 sample xml

- cx.xsd   

 XML Schema which was generated using trang command on Debian Linux and modified manually.


Trang
=====

trang_ is a Java based XML tool to generate and convert XML Schema and Relax NG.

.. _trang: http://www.thaiopensource.com/relaxng/trang.html 

Install Trang on Debian Squeeze
-------------------------------

Simple. Just use aptitude command:

    sudo apatitude install trang -y

More than 100Mbytes space is required.

Generate XML Schema
---------------------

Execute the following command:

    % trang -I xml -O xsd cx.xml cx.xsd

