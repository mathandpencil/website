PIPELINE_JS = { 
    'global': {
        'source_filenames': (   
            'js/vendor/jquery-1.8.3.js',
            'js/vendor/classie.js',  
            'js/vendor/modernizr.js',  
            'js/vendor/slide_menu.js', 
            'js/vendor/jquery.validate.js',
 
        ),
        'output_filename': 'js/bundle-global.js',
    },  
}

PIPELINE_CSS = {
	'global': {
		'source_filenames': (
			'css/reset.css',
			'css/icons.css',
			'css/default.css',
			'css/header.css',
			'css/buttons.css',
			'css/grid.css',
			'css/grid_items.css',
			'css/forms.css',
			'css/pagination.css',
			'css/slide_menu.css',
			'css/landing.css'
		),
		'output_filename': 'css/bundle-global.css',
	},
}
