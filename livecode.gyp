{
	'includes':
	[
		'common.gypi',
	],
	
	'targets':
	[
		{
			'target_name': 'LiveCode-all',
			'type': 'none',
			
			'dependencies':
			[
				# Engines
				'engine/engine.gyp:standalone',

				# The revsecurity library is an output and not an intermediate product
				'thirdparty/libopenssl/libopenssl.gyp:revsecurity',
				
				# Externals
				'revdb/revdb.gyp:revdb',
				'revdb/revdb.gyp:dbmysql',
				'revdb/revdb.gyp:dbsqlite',
				'revpdfprinter/revpdfprinter.gyp:revpdfprinter',
				'revxml/revxml.gyp:revxml',
				'revzip/revzip.gyp:revzip',
			],
			
			'conditions':
			[
				[
					'mobile == 0',
					{
						'dependencies':
						[
							# Engines
							'engine/engine.gyp:development',
							'engine/engine.gyp:installer',
							'engine/engine.gyp:server',
							
							# Externals
							'revbrowser/revbrowser.gyp:revbrowser',
							'revbrowser/revbrowser.gyp:revbrowser-cefprocess',
							'revdb/revdb.gyp:dbodbc',
							'revdb/revdb.gyp:dbpostgresql',
							'revfont/revfont.gyp:revfont',
							'revmobile/revmobile.gyp:revandroid',
							'revmobile/revmobile.gyp:reviphone',
							'revspeech/revspeech.gyp:revspeech',
							'revvideograbber/revvideograbber.gyp:revvideograbber',
							
							# Server externals
							'revdb/revdb.gyp:revdb-server',
						],
					},
				],
				[
					'OS == "ios"',
					{
						'dependencies':
						[
							'engine/engine.gyp:standalone-mobile-lib-community',
						],
					},
				],
			],
		},
		
		{
			'target_name': 'binzip-copy',
			'type': 'none',
			
			'dependencies':
			[
				'LiveCode-all',
			],
			
			'copies':
			[{
				'destination': '<(output_dir)',
				'files': [ '>@(dist_files)' ],
			}],
		},
	],
}