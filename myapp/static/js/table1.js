$(function(){
    getHt();
    table();
})
//获取div的高度
function getHt(){
   var all_height=$(window).height();
   var div_height=all_height-80;
    $("#car_control").css("height",div_height+"px");


}
//表格部分
function table(){
    $('#table').bootstrapTable({
        method: "get",
        url: "../json/case.json",
        striped: true,
        singleSelect: false,
        dataType: "json",
        pagination: true, //分页
        pageSize: 10,
        pageNumber: 1,
        search: false, //显示搜索框
        contentType: "application/x-www-form-urlencoded",
        queryParams: null,
        //sidePagination: "server", //服务端请求
        columns: [
            {
                title: "",
                field: 'ch',
                align: 'center',
                width:'30px',
                valign: 'middle',
                formatter:function(val,row){
                    return '<div class="cliclRed"></div>';
                }
            }
            ,
            {
                title: "事项名称",
                field: 'name',
                align: 'center',
                valign: 'middle'
            },
            {
                title: '负责部门',
                field: 'part',
                align: 'center',
                valign: 'middle'
            },
            {
                title: '上传日期',
                field: 'time',
                align: 'center',
                valign: 'middle'
            },

            {
                title: '操作',
                field: 'opear',
                width:'250px',
                align: 'center',
                formatter: function (value, row) {
                    var e = '<a  href="../../templates/tail_more.html" class="table_edit" title="咨询" onclick="edit(\'' + row.id + '\')">详情</a> ';
                    var c = '<a   href="javascript:void(0)" class="table_del" title="删除" onclick="del(\'' + row.id + '\')">删除</a> ';
                    return e+c ;
                }
            }
        ]
    });
}
 function add(){
     layer.open({
         type: 2,
         skin: 'demo-class',
         title: '详情页面',
         fix: true,
         shadeClose: true,
         area: ['1000px', '500px'],
         content: '../../templates/tail_sm.html',
     });
 }
function edit(){
    layer.open({
        type: 2,
        skin: 'layui-layer-lan',
        title: '详情页面',
        fix: true,
        shadeClose: true,
        area: ['1100px', '600px'],
        content: '../../templates/tail_more.html',
    });
}
function openList(){
    $(".find_expend").show();
    $("#open").hide();
}
function closeList(){
    $(".find_expend").hide();
    $("#open").show();
}