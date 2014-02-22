var ImagebaseRouter = Backbone.Router.extend({

    routes: {
        'image/:id/': 'viewImageDetail'
    },

    'viewImageDetail': function(id){
        console.log('load image %s:',id);
    }

});


$(function(){

    var imagebaseRouter = new ImagebaseRouter();

    $('a[data-internal]').on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        console.log('e.currentTarget.pathname:', e.currentTarget.pathname);
        imagebaseRouter.navigate(e.currentTarget.pathname, {trigger: true});
    });

    Backbone.history.start({pushState: true});

});






























$(document).foundation();