var path = require('path')

// A factory function that generates a new view which handles generic rendering of
// a template.
function template_factory(template_name)
{
	return function(req, res)
	{
		res.writeHead(200, {'Content-Type': 'text/html'})

		res.render(template_name, {}, function(data){
			res.end(data)
		}, {
			template_dirs: [path.resolve('.') + '/templates']
		})
	}
}

exports.homepage = template_factory('home.jade')
exports.about = template_factory('about.jade')

