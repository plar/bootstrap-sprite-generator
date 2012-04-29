#!/usr/bin/python
# -*- coding: utf-8 -*-

import fnmatch
import os

"""
Icon Library Interface
"""
class IconFilter(object):
    '''
    Abstract base class for Icon Filters
    '''

    def __init__(self, id, prefix, types, default_icon_dir, default_output_dir):
        super(IconFilter, self).__init__()
        self._id = id
        self._prefix = prefix
        self._types = types
        self._default_output_dir = default_output_dir
        self._default_icon_dir = default_icon_dir
        self._adjust_map = None

    @property
    def id(self):
        return self._id

    @property
    def prefix(self):
        return self._prefix

    """
    Return list of supported filter types
    """
    @property
    def types(self):
        return self._types
    
    @property
    def default_icon_dir(self):
        return self._default_icon_dir

    @property
    def default_output_dir(self):
        return self._default_output_dir

    """
    Filter callback
    return
        None if not matched
        tuple(file_name, icon_name)
    """
    def icon_name(self, filter_type, file_name):
        raise NotImplementedError()
    
    @property
    def adjusted_file_names(self):
        if not self._adjust_map:
            self._adjust_map = dict()
            for img in self._raw_adjust_map:
                (file_name, icon_name) = img.split(":")
                self._adjust_map[file_name] = icon_name

        return self._adjust_map

    def adjust_icon_name(self, file_name, icon_name):
        if not icon_name:
            return None
        
        # adjust icon name
        if file_name in self.adjusted_file_names:
            old_icon_name = icon_name
            icon_name = self.adjusted_file_names[file_name]
            print "%s: adjust icon name '%s' to '%s'" % (file_name, old_icon_name, icon_name)

        return icon_name

"""
Icon Generic Filter
"""
class GenericIconFilter(IconFilter):
    def __init__(self, adjust_map=None):
        super(GenericIconFilter, self).__init__(
            id="GenericFilter", 
            prefix="gn", 
            types=["all"],
            default_icon_dir="generic_input",
            default_output_dir="generic_output")

    def icon_name(self, filter_type, file_name):
        (root, unused) = os.path.splitext(file_name)
        return root

"""
Icon Glyph Icons v1.7pro Filter  
http://glyphicons.com/
"""    
class GlyphIconFilter(IconFilter):

    def __init__(self, adjust_map=None):
        super(GlyphIconFilter, self).__init__(
            id="GlyphIconFilter", 
            prefix="gi", 
            types=["normal", "large"],
            default_icon_dir="glyphicons_pro/glyphicons/png",
            default_output_dir="glyphicons_output")

        if  adjust_map is None:
            self._raw_adjust_map = [
                "glyphicons_073_signal.png:signal-radar", "glyphicons_079_signal.png:signal-network",
                "glyphicons_091_adjust.png:adjust-contrast", "glyphicons_119_adjust.png:adjust-eq",
                "glyphicons_222_share.png:share-arrow", "glyphicons_326_share.png:share-point",
                
                "glyphicons_073_signal@2x.png:signal-radar", "glyphicons_079_signal@2x.png:signal-network",
                "glyphicons_091_adjust@2x.png:adjust-contrast", "glyphicons_119_adjust@2x.png:adjust-eq",
                "glyphicons_222_share@2x.png:share-arrow", "glyphicons_326_share@2x.png:share-point",
                ]
        else:
            self._raw_adjust_map = adjust_map
        
    def icon_name(self, filter_type, file_name):
        if filter_type not in self.types or not fnmatch.fnmatch(file_name, "*.png"):
            return None
        
        # validate file name for icon_type
        (root, unused) = os.path.splitext(file_name)
        parts = "-".join(root.split("_")[2:])
        is_large = root.endswith("@2x")
        if filter_type == 'large' and is_large:
            return self.adjust_icon_name(file_name, parts[:-3]) # strip @2x from 
        elif filter_type == 'normal' and not is_large:
            return self.adjust_icon_name(file_name, parts)
            
        return None
    
