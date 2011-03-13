var url = require('zest/http/urls').url

exports.url_patterns = [
	url(/^\/$/, 'monokro.me/views:homepage', []),
]

