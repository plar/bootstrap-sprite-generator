Bootstrap Sprite Generator
==========================

Generate <a href="http://twitter.github.com/bootstrap/">twitter bootstrap</a> sprite files for different icon libraries.
<br/>Supported icon libraries: <a href="http://glyphicons.com">Glyph Icon</a>, <a href="http://p.yusukekamiyamane.com/">Figue Icons</a> and Generic Folders :)

I bought Glyph Icons Pro Library recently and found 
that it is really hard to create <a href="https://github.com/twitter/bootstrap/blob/master/less/sprites.less">sprite.less</a> file and <a href="https://github.com/twitter/bootstrap/blob/master/img/glyphicons-halflings.png">sprite image</a> file for 400 icons. I am not a designer and I do not have 
PS or other tools to generate big sprite file from list of small files. 

So, that is why I have created that python script.

Usage example
=============

Generate sprite image and sprite.less files for Glyph Icons library
-------------------------------------------------------------------

1. mkdir ~/icons
2. git clone git://github.com/plar/bootstrap-sprite-generator.git ~/icons
3. cd ~/icons
4. unzip glyphicons_pro.zip -d ~/icons<br/> 
5. cd ~/icons
6. ./bootstrap_sprite_generator.py -t gi:normal 

<pre>
Load icons(normal) from glyphicons_pro/glyphicons/png directory...
glyphicons_073_signal.png: adjust icon name 'signal' to 'signal-radar'
glyphicons_079_signal.png: adjust icon name 'signal' to 'signal-network'
glyphicons_091_adjust.png: adjust icon name 'adjust' to 'adjust-contrast'
glyphicons_119_adjust.png: adjust icon name 'adjust' to 'adjust-eq'
glyphicons_222_share.png: adjust icon name 'share' to 'share-arrow'
glyphicons_326_share.png: adjust icon name 'share' to 'share-point'
Total icons(normal): 400
Tile size: 36px x 30px
Sprite image size in tiles: 20x20
Sprite image size in pixels: 720x600
Creating sprite image glyphicons_output/sprites-pro.png...
Done
Creating sprite css glyphicons_output/sprites-pro.less...
Done
</pre>

If you want to resize icons to smaller size you can use -r argument.

ie: ./bootstrap_sprite_generator.py -t gi:normal -r 24<br/>
All icons will be resized to 24x24 pixels if they aren't already and the sprite image and css files 
will be generated with the new icon sizes.

Generic generator
-----------------
You can generate sprite image file and sprite css file for any set of icons. 
For example if you have fugue-icons in ~/icons/fugue-icons-3.0/icons directory then you can run generator as:

./bootstrap_sprite_generator.py -t gn:all -d ~/icons/fugue-icons-3.0/icons -o ~/icons/fugue-output

<pre>
Load icons(all) from ~/icons/fugue-icons-3.0/icons directory...
Total icons(all): 3000
Tile size: 16px x 16px
Sprite image size in tiles: 55x55
Sprite image size in pixels: 880x880
Creating sprite image ~/icons/fugue-output/sprites-pro.png...
Done
Creating sprite css ~/icons/fugue-output/sprites-pro.less...
Done
</pre>


CLI Help
========

<pre>
usage: bootstrap_sprite_generator.py [options]

Generate bootstrap sprite files for different icon libraries.

optional arguments:
  -h, --help            show this help message and exit
  -d ICON_DIR           icon files directory
  -o OUTPUT_DIR         result files directory. if directory does not exist, 
                        it will be created automatically.
  -r RESIZE             resize original library icons to specific size(pixels)
  -m ADJUST_MAP         adjust icon name for specific file. It option can be
                        used multiply times. 
                        ie: -m glyphicons_079_signal.png:signal-strength
  -t {gi:normal,gi:large,gn:all}
                        sprite generator type

</pre>