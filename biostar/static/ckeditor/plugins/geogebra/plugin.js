/*
* geogebra Embed Plugin
*
* @author Jonnas Fonini <contato@fonini.net>
* @version 2.0.4
*/
( function() {
	CKEDITOR.plugins.add( 'geogebra',
	{
		lang: [ 'en', 'ru'],
		init: function( editor )
		{
			editor.addCommand( 'geogebra', new CKEDITOR.dialogCommand( 'geogebra', {
				allowedContent: 'iframe[!scrolling,!width,!height,!src,!style]; object param[*]'
			}));

			editor.ui.addButton( 'Geogebra',
			{
				label : editor.lang.geogebra.button,
				toolbar : 'insert',
				command : 'geogebra',
				icon : this.path + 'images/icon.png'
			});

			CKEDITOR.dialog.add( 'geogebra', function ( instance )
			{
				var video;

				return {
					title : editor.lang.geogebra.title,
					minWidth : 500,
					minHeight : 200,
					contents :
						[{
							id : 'geogebraPlugin',
							expand : true,
							elements :
								[{
									id : 'geoEmbed',
									type : 'textarea',
									label : editor.lang.geogebra.geoEmbed,
									autofocus : 'autofocus',

									validate : function ()
									{
										if ( this.isEnabled() )
										{
											if ( !this.getValue() )
											{
												alert( editor.lang.geogebra.noCode );
												return false;
											}
											else
											if ( this.getValue().length === 0 )
											{
												alert( editor.lang.geogebra.invalidEmbed );
												return false;
											}
										}
									}
								},
                                {
                                    type : 'text',
                                    id : 'txtWidth',
                                    width : '60px',
                                    label : editor.lang.geogebra.txtWidth,
                                    'default' : editor.config.geogebra_width != null ? editor.config.geogebra_width : '640',
                                    validate : function ()
                                    {
                                        if ( this.getValue() )
                                        {
                                            var width = parseInt ( this.getValue() ) || 0;

                                            if ( width === 0 )
                                            {
                                                alert( editor.lang.geogebra.invalidWidth );
                                                return false;
                                            }
                                        }
                                        else {
                                            alert( editor.lang.geogebra.noWidth );
                                            return false;
                                        }
                                    }
                                },
                                {
                                    type : 'text',
                                    id : 'txtHeight',
                                    width : '60px',
                                    label : editor.lang.geogebra.txtHeight,
                                    'default' : editor.config.geogebra_height != null ? editor.config.geogebra_height : '360',
                                    validate : function ()
                                    {
                                        if ( this.getValue() )
                                        {
                                            var height = parseInt ( this.getValue() ) || 0;

                                            if ( height === 0 )
                                            {
                                                alert( editor.lang.geogebra.invalidHeight );
                                                return false;
                                            }
                                        }
                                        else {
                                            alert( editor.lang.geogebra.noHeight );
                                            return false;
                                        }
                                    }
								},
								{
									type : 'hbox',
									widths : [ '100%' ],
									children :
										[
											{
												id : 'showGeoToolbar',
												type : 'checkbox',
												label : editor.lang.geogebra.showGeoToolbar,
												'default' : editor.config.geogebra_responsive != null ? editor.config.geogebra_responsive : false
											}
										]
								},
							]
						}
					],
					onOk: function()
					{
						var content = '';

						if ( this.getContentElement( 'geogebraPlugin', 'geoEmbed' ).isEnabled() )

							var raw_url = this.getValueOf( 'geogebraPlugin', 'geoEmbed' );
							var width = this.getValueOf( 'geogebraPlugin', 'txtWidth' );
							var height = this.getValueOf( 'geogebraPlugin', 'txtHeight' );

                            var url = raw_url.match(/.*src="(.+?)".*/);
                            var new_url = url[1];

                            if (width) {
                                new_url = new_url.replace(/(.*\/width\/)\d+?(\/.*)/,'$1'+ width + '$2')
                            }
                            if (height) {
                                new_url = new_url.replace(/(.*\/height\/)\d+?(\/.*)/,'$1'+ height + '$2')
                            }

							if ( this.getContentElement( 'geogebraPlugin', 'showGeoToolbar').getValue() === true ) {
								new_url = new_url.replace(/(.*\/smb\/).+?(\/.*)/,'$1'+ true + '$2')
								new_url = new_url.replace(/(.*\/stb\/).+?(\/.*)/,'$1'+ true + '$2')

						    }

                            content = '<iframe scrolling="no" src="' + new_url +'" width="'+ width + 'px" height="' + height + 'px" style="border:0px;"> </iframe>';

						var element = CKEDITOR.dom.element.createFromHtml( content );
						var instance = this.getParentEditor();
						instance.insertElement(element);
					}
				};
			});
		}
	});
})();
