$("#CtoSButton").click(function ( ){
    return $.ajax({
        url: '/Trades'
        ,type: 'GET'
    })
});