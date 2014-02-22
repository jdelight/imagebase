// hacked jquery to add a sendDelay property
$.ajaxSetup({
    sendDelay: 1000,
    timeout: 2000
});

var ImagebaseRouter = Backbone.Router.extend({

    routes: {
        'image/:id/': 'viewImageDetail'
    },

    viewImageDetail: function(id){
        console.log('load image %s', id);
        //$('#image-detail-container').load('/image/'+id+'/');
        $('#image-detail-container').load('/image/'+id+'/content/');
    }

});


$(function(){
    // create our router instance
    var imagebaseRouter = new ImagebaseRouter();

    // intercept links with the data-internal attributes and navigate using the router
    $('a[data-internal]').on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        imagebaseRouter.navigate(e.currentTarget.pathname, {trigger: true});
    });

    // start listening to url changes (with pushState)
    Backbone.history.start({pushState: true});
});

