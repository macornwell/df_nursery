root.df = root.df ? {}

class TaxonomyDAL
  __root_url = 'http://openfruit.io/api/v1/'

  constructor:()->

  cultivarLookahead:(cultivar_name)=>
    url = __root_url + 'cultivars?name=' + cultivar_name




setup_ajax_post = ()=>
  csrftoken = $.cookie('csrftoken')
  $.ajaxSetup({
    beforeSend: (xhr, settings) => xhr.setRequestHeader("X-CSRFToken", csrftoken)
  })

root.df.setup_ajax_post = setup_ajax_post
root.df.TaxonomyDAL = TaxonomyDAL