/*大屏*/
$(function(){
    initMap();
})
//地图界面高度设置



//加载地图
function initMap(){
// 百度地图API功能
    var map = new BMap.Map("map_div");    // 创建Map实例
    map.centerAndZoom(new BMap.Point(121.632654, 29.9318922), 19);  // 初始化地图,设置中心点坐标和地图级别
    //添加地图类型控件
    var size1 = new BMap.Size(10, 50);
    map.addControl(new BMap.MapTypeControl({
        offset: size1,
        mapTypes:[
            BMAP_NORMAL_MAP,
            BMAP_HYBRID_MAP,

        ]}));
    // 编写自定义函数,创建标注
    function addMarker(point){
        var marker = new BMap.Marker(point);
        map.addOverlay(marker);
    }
    var points = [
        new BMap.Point(121.633376, 29.9319999),new BMap.Point(121.632633, 29.9318677),
        new BMap.Point(121.632324, 29.9315232),new BMap.Point(121.632187, 29.9316457),
        new BMap.Point(121.632943, 29.9313022),new BMap.Point(121.632654, 29.9316678),
        new BMap.Point(121.632347, 29.9316232),new BMap.Point(121.632176, 29.9318567),
        new BMap.Point(121.632763, 29.9315456),new BMap.Point(121.632512, 29.9318657),
        new BMap.Point(121.632147, 29.9316574),new BMap.Point(121.632145, 29.9312138),
        new BMap.Point(121.632421, 29.9313267),new BMap.Point(121.632545, 29.9313543),
        new BMap.Point(121.632876, 29.9315765),new BMap.Point(121.633445, 29.9315237),
        new BMap.Point(121.632645, 29.9313867),new BMap.Point(121.632346, 29.9315382),
        new BMap.Point(121.632762, 29.9312564),new BMap.Point(121.632774, 29.9311852),
        new BMap.Point(121.632762, 29.9314964),new BMap.Point(121.632967, 29.9312546),
        new BMap.Point(121.632978, 29.9311325),new BMap.Point(121.632889, 29.9313865),
        new BMap.Point(121.632495, 29.9319654),new BMap.Point(121.632967, 29.9316523),
        new BMap.Point(121.633999, 29.9319745),new BMap.Point(121.632465, 29.9318564),
        new BMap.Point(121.633196, 29.9311674),new BMap.Point(121.633212, 29.9315763),
        new BMap.Point(121.633999, 29.9319655),new BMap.Point(121.632122, 29.9316534),
        new BMap.Point(121.632042, 29.9311567),new BMap.Point(121.632865, 29.9319745),
        new BMap.Point(121.632956, 29.9311876),new BMap.Point(121.632123, 29.9313544),
        new BMap.Point(121.633398, 29.9311575),new BMap.Point(121.632233, 29.9317456),
        new BMap.Point(121.632999, 29.9313534),new BMap.Point(121.632144, 29.9314742),
        new BMap.Point(121.632645, 29.9313657),new BMap.Point(121.632100, 29.9311236),
        new BMap.Point(121.632856, 29.9311768),new BMap.Point(121.632032, 29.9312634),
        new BMap.Point(121.632654, 29.9314534),new BMap.Point(121.632089, 29.9316556),
        new BMap.Point(121.633654, 29.9316436),new BMap.Point(121.632043, 29.9317645),
        new BMap.Point(121.633933, 29.9318796),new BMap.Point(121.633376, 29.9315745),
        new BMap.Point(121.633654, 29.9311766),new BMap.Point(121.632657, 29.9317456),
        new BMap.Point(121.633345, 29.9313476),new BMap.Point(121.632767, 29.9313655),
        new BMap.Point(121.633121, 29.9318976),new BMap.Point(121.632564, 29.9318643),
        new BMap.Point(121.633763, 29.9312314),new BMap.Point(121.632967, 29.9316345),
        new BMap.Point(121.633291, 29.9314234),new BMap.Point(121.632542, 29.9317455),
        new BMap.Point(121.633244, 29.9317894),new BMap.Point(121.633041, 29.9315745),
        new BMap.Point(121.633595, 29.9318877),new BMap.Point(121.633076, 29.9318954),
        new BMap.Point(121.633008, 29.9319324),new BMap.Point(121.633034, 29.9314544),
        new BMap.Point(121.633376, 29.9315987),new BMap.Point(121.633089, 29.9315234),
        new BMap.Point(121.633644, 29.9317823),new BMap.Point(121.633085, 29.9316755),
        new BMap.Point(121.633543, 29.9313432),new BMap.Point(121.633011, 29.9318657),
        new BMap.Point(121.633734, 29.9316565),new BMap.Point(121.633222, 29.9319898),
        new BMap.Point(121.633867, 29.9315673),new BMap.Point(121.633523, 29.9312253),
        new BMap.Point(121.633764, 29.9318786),new BMap.Point(121.633876, 29.9312357),
        new BMap.Point(121.633942, 29.9312087),new BMap.Point(121.633312, 29.9316792),
        new BMap.Point(121.633644, 29.9319455),new BMap.Point(121.633176, 29.9314545),
        new BMap.Point(121.632564, 29.9315435),new BMap.Point(121.633623, 29.9319347),
        new BMap.Point(121.632124, 29.9317435),new BMap.Point(121.633212, 29.9318537),
        new BMap.Point(121.632634, 29.9313543),new BMap.Point(121.632176, 29.9314866),
        new BMap.Point(121.632376, 29.9317897),new BMap.Point(121.632231, 29.9312973),
        new BMap.Point(121.633345, 29.9314566),new BMap.Point(121.633978, 29.9317686),
        new BMap.Point(121.632764, 29.9316456),new BMap.Point(121.632169, 29.9311544),
        new BMap.Point(121.633432, 29.9313247),new BMap.Point(121.632537, 29.9314565),
        new BMap.Point(121.632526, 29.9319783),new BMap.Point(121.633869, 29.9314674),
        new BMap.Point(121.632867, 29.9314765),new BMap.Point(121.632898, 29.9319784),
        new BMap.Point(121.632777, 29.9317658),new BMap.Point(121.633856, 29.9317456),
        new BMap.Point(121.633368, 29.9316856),new BMap.Point(121.633376, 29.9311275),
        new BMap.Point(121.632434, 29.9313438),new BMap.Point(121.633867, 29.9315675),
        new BMap.Point(121.632567, 29.9312567),new BMap.Point(121.633321, 29.9315423),
        new BMap.Point(121.633543, 29.9318903),new BMap.Point(121.633763, 29.9316454),
        new BMap.Point(121.632514, 29.9312434),new BMap.Point(121.633557, 29.9317567),
        new BMap.Point(121.632867, 29.9313654),new BMap.Point(121.633865, 29.9312345),
        new BMap.Point(121.632376, 29.9315867),new BMap.Point(121.633967, 29.9316787),
        new BMap.Point(121.632645, 29.9314867),new BMap.Point(121.633213, 29.9316435),
        new BMap.Point(121.633765, 29.9314978),new BMap.Point(121.633978, 29.9317456),
        new BMap.Point(121.632987, 29.9318799),new BMap.Point(121.633755, 29.9313467),
        new BMap.Point(121.632375, 29.9313467),new BMap.Point(121.633567, 29.9316784),
    ];

    // 循环添加标记
    for (var i = 0; i < points.length; i++) {
        addMarker(points[i]);
    }

    var polygon = new BMapGL.Polygon([
        new BMapGL.Point(121.6337112,39.920977),
        new BMapGL.Point(116.385243,39.913063),
        new BMapGL.Point(116.394226,39.917988),
        new BMapGL.Point(116.401772,39.921364),
        new BMapGL.Point(116.41248,39.927893)
    ], {strokeColor:"blue", strokeWeight:2, strokeOpacity:0.5});
    map.addOverlay(polygon);

    map.setCurrentCity("宁波");          // 设置地图显示的城市 此项是必须设置的
    map.enableScrollWheelZoom(true);     //开启鼠标滚轮缩放


//加载城市控件
    var size = new BMap.Size(10, 50);
    map.addControl(new BMap.CityListControl({
        anchor: BMAP_ANCHOR_TOP_LEFT,
        offset: size,


    }));
}

