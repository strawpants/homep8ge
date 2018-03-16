// Load Charts and the corechart package.

google.charts.load('current', {packages: ['corechart']});
    google.charts.setOnLoadCallback(QueryGdata);

    function QueryGdata() {
    var queryString = encodeURIComponent('SELECT B LIMIT 20');
    var URL='https://docs.google.com/spreadsheets/d/1tTW2rUl8CQWC39XV_2Rj_qnZgqmiOGtNfRN0VMDuVOE/gviz/tq?gid=0&tq=';

    var query=new google.visualization.Query(URL+queryString);
    query.send(handleQueryResponse); 

 }


function  handleQueryResponse(response){
    if (response.isError()) {
        alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
      }
        
      var data=countOccurences(response.getDataTable());
      
      // Instantiate and draw the chart.
      var chart = new google.visualization.PieChart(document.getElementById('chart_test'));
       var opt={title:'Division'}
      chart.draw(data, opt);
}

//function to count occurences in a google datatable column
function countOccurences(inarr){
    var dt=new google.visualization.DataTable();
    //first column contains unique entries
    dt.addColumn(inarr.getColumnType(0),inarr.getColumnLabel(0));
    //second column the number of occurences
    dt.addColumn('number','Occurences');
    
    var distinct=inarr.getDistinctValues(0);
    
    for(var i=0; i< distinct.length;++i){
        //possibly skip null entries
        if (distinct[i]== null){
            continue;
        }
       dt.addRow([distinct[i],0]);
    }

        
    var len=inarr.getNumberOfRows();
    for(var j=0;j<len;++j){
        for (var i=0;i<dt.getNumberOfRows();++i){
            if (dt.getValue(i,0) == inarr.getValue(j,0)){
                    //increase count
                    var cnt=dt.getValue(i,1)+1
                    dt.getValue(i,1,cnt);          
                    break;
            }

        }
    }

    return dt
    
}