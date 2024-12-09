window.onload = function () {

    const option0={grid:{left:'5%',right:'15%',top:'10%',bottom:'5%',containLabel:true},backgroundColor:'transparent',color:['#EF9A9A','#F48FB1','#CE93D8','#F3E5F5','#EDE7F6'],series:[{label:{normal:{fontSize:18}},type:'pie',center:['50%','50%'],data:[{value:439,name:'0-300元'},{value:1607,name:'300-2000元'},{value:226,name:'2000-5000元'},{value:204,name:'5000-10000元'},{value:119,name:'10000元以上'}],itemStyle:{shadowColor:'rgba(255,255,255,0.25)',shadowBlur:10}}]}
    const chart0 = echarts.init(document.getElementById('chart0'))
    chart0.setOption(option0)

    const chart1 = echarts.init(document.getElementById('chart1'))
    const option1={grid:{left:'5%',right:'15%',top:'10%',bottom:'5%',containLabel:true},xAxis:{data:['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月'],axisTick:{show:false},axisLabel:{color:'white',fontFamily:'Light',fontSize:16},axisLine:{lineStyle:{color:'white'}},axisTick:{lineStyle:{color:'white'}}},yAxis:{axisLabel:{color:'white',fontFamily:'Light',fontSize:16},axisLine:{lineStyle:{color:'white'}},axisTick:{lineStyle:{color:'white'}},},series:[{type:'line',symbol:"circle",symbolSize:10,smooth:true,data:[300,400,350,500,600,500,700,700,600,800,450,350],itemStyle:{color:"rgba(255,255,255,1)",borderWidth:1,borderColor:"rgba(87, 183, 242, 1)"},lineStyle:{width:3,color:"rgba(87, 183, 242, 1)"},areaStyle:{color:{type:'linear',x:0,y:0,x2:0,y2:1,colorStops:[{offset:0,color:'rgba(87, 183, 242, 1)'},{offset:1,color:'rgba(6,37,55,0)'}],global:false}}}]}
    chart1.setOption(option1)

    const chart2 = echarts.init(document.getElementById('chart2'))
    const option2={grid:{left:'5%',right:'15%',top:'10%',bottom:'5%',containLabel:true},xAxis:{type:'category',boundaryGap:[0,0.01],data:['平遥古城', '云冈石窟', '五台山', '晋祠', '大同古城', '长治天脊山', '王家大院', '壶口瀑布', '临汾尧山', '介休绵山'],axisLabel:{color:'white',fontFamily:'Light',fontSize:16},axisLine:{lineStyle:{color:'white'}},axisTick:{lineStyle:{color:'white'}},},yAxis:{type:'value',axisLabel:{color:'white',fontFamily:'Light',fontSize:16},name:'单位：万人',axisLine:{lineStyle:{color:'white'}},axisTick:{lineStyle:{color:'white'}},splitLine:{show:true,lineStyle:{color:['white'],width:1,type:'solid'}}},series:[{type:'bar',barMaxWidth:'50%',itemStyle:{normal:{color:{type:'linear',x:0,y:0,x2:0,y2:1,colorStops:[{offset:0,color:'rgba(87, 183, 242, 1)'},{offset:1,color:'rgba(6,37,55,0)'}],global:false}}},data:[831,823,712,632,612,522,484,454,413,403,345]}]}
    chart2.setOption(option2)

    const chart3 = echarts.init(document.getElementById('chart3'))
    const option3={grid:{left:'5%',right:'15%',top:'10%',bottom:'5%',containLabel:true},xAxis:{type:'category',boundaryGap:[0,0.01],data:['平遥古城', '云冈石窟', '五台山', '晋祠', '长治天脊山', '王家大院', '介休绵山', '壶口瀑布', '大同古城', '临汾尧山'],axisLabel:{color:'white',fontFamily:'Light',fontSize:16},axisLine:{lineStyle:{color:'white'}},axisTick:{lineStyle:{color:'white'}},},yAxis:{type:'value',axisLabel:{color:'white',fontFamily:'Light',fontSize:16},name:'评分',axisLine:{lineStyle:{color:'white'}},axisTick:{lineStyle:{color:'white'}},splitLine:{show:true,lineStyle:{color:['white'],width:1,type:'solid'}}},series:[{type:'bar',barMaxWidth:'50%',itemStyle:{normal:{color:{type:'linear',x:0,y:0,x2:0,y2:1,colorStops:[{offset:0,color:'rgba(87, 183, 242, 1)'},{offset:1,color:'rgba(6,37,55,0)'}],global:false}}},data:[9.7,9.6,9.6,9.5,9.5,9.5,9.4,9.4,9.4,9.4,9.3]}]}
    chart3.setOption(option3)


    function fillZero(str) {
        let realNum
        if(str < 10) {
            realNum	= '0'+str
        } else {
            realNum	= str
        }
        return realNum
    }

    function getTime() {
        const dateTime = new Date()
        const year = dateTime.getFullYear() //获取完整的年份(4位,1970-????)
        const month = dateTime.getMonth() + 1 //获取当前月份(0-11,0代表1月)
        const today = dateTime.getDate() //获取当前日(1-31)
        const day = dateTime.getDay() //获取当前星期X(0-6,0代表星期天)
        const hour = dateTime.getHours() //获取当前小时数(0-23)
        const minute = dateTime.getMinutes() //获取当前分钟数(0-59)
        const second = dateTime.getSeconds() //获取当前秒数(0-59)
        const week = ['Sun.', 'Mon.', 'Tues.', 'Wen.', 'Thur.', 'Fri.', 'Sat.']

        const currentTime = year+'-'+fillZero(month)+'-'+fillZero(today)+'&nbsp;&nbsp;'+fillZero(hour)+':'+fillZero(minute)+':'+fillZero(second)+'&nbsp;&nbsp;'+week[day]+'&nbsp;&nbsp;'
        document.querySelector('#timer').innerHTML = currentTime
    }
    setInterval(getTime, 1000)
    /*const mapOption = {backgroundColor:'transparent',tooltip:{trigger:'item'},geo:{map:'map',zoom:1.2,roam:false,emphasis:{itemStyle:{areaColor:'#0DC0FF99'},label:{show:true,color:'#fff'}},itemStyle:{borderWidth:1,borderColor:'#0DC0FF',areaColor:'#092766',shadowBlur:10,label:{show:true,textStyle:{color:'#fff',fontWeight:'bold'}}}}}
    const adcode = {北京市:'110000',天津市:'120000',河北省:'130000',石家庄市:'130100',唐山市:'130200',秦皇岛市:'130300',邯郸市:'130400',邢台市:'130500',保定市:'130600',张家口市:'130700',承德市:'130800',沧州市:'130900',廊坊市:'131000',衡水市:'131100',山西省:'140000',太原市:'140100',大同市:'140200',阳泉市:'140300',长治市:'140400',晋城市:'140500',朔州市:'140600',晋中市:'140700',运城市:'140800',忻州市:'140900',临汾市:'141000',吕梁市:'141100',内蒙古自治区:'150000',呼和浩特市:'150100',包头市:'150200',乌海市:'150300',赤峰市:'150400',通辽市:'150500',鄂尔多斯市:'150600',呼伦贝尔市:'150700',巴彦淖尔市:'150800',乌兰察布市:'150900',兴安盟:'152200',锡林郭勒盟:'152500',阿拉善盟:'152900',辽宁省:'210000',沈阳市:'210100',大连市:'210200',鞍山市:'210300',抚顺市:'210400',本溪市:'210500',丹东市:'210600',锦州市:'210700',营口市:'210800',阜新市:'210900',辽阳市:'211000',盘锦市:'211100',铁岭市:'211200',朝阳市:'211300',葫芦岛市:'211400',吉林省:'220000',长春市:'220100',吉林市:'220200',四平市:'220300',辽源市:'220400',通化市:'220500',白山市:'220600',松原市:'220700',白城市:'220800',延边朝鲜族自治州:'222400',黑龙江省:'230000',哈尔滨市:'230100',齐齐哈尔市:'230200',鸡西市:'230300',鹤岗市:'230400',双鸭山市:'230500',大庆市:'230600',伊春市:'230700',佳木斯市:'230800',七台河市:'230900',牡丹江市:'231000',黑河市:'231100',绥化市:'231200',大兴安岭地区:'232700',上海市:'310000',江苏省:'320000',南京市:'320100',无锡市:'320200',徐州市:'320300',常州市:'320400',苏州市:'320500',南通市:'320600',连云港市:'320700',淮安市:'320800',盐城市:'320900',扬州市:'321000',镇江市:'321100',泰州市:'321200',宿迁市:'321300',浙江省:'330000',杭州市:'330100',宁波市:'330200',温州市:'330300',嘉兴市:'330400',湖州市:'330500',绍兴市:'330600',金华市:'330700',衢州市:'330800',舟山市:'330900',台州市:'331000',丽水市:'331100',安徽省:'340000',合肥市:'340100',芜湖市:'340200',蚌埠市:'340300',淮南市:'340400',马鞍山市:'340500',淮北市:'340600',铜陵市:'340700',安庆市:'340800',黄山市:'341000',滁州市:'341100',阜阳市:'341200',宿州市:'341300',六安市:'341500',亳州市:'341600',池州市:'341700',宣城市:'341800',福建省:'350000',福州市:'350100',厦门市:'350200',莆田市:'350300',三明市:'350400',泉州市:'350500',漳州市:'350600',南平市:'350700',龙岩市:'350800',宁德市:'350900',江西省:'360000',南昌市:'360100',景德镇市:'360200',萍乡市:'360300',九江市:'360400',新余市:'360500',鹰潭市:'360600',赣州市:'360700',吉安市:'360800',宜春市:'360900',抚州市:'361000',上饶市:'361100',山东省:'370000',济南市:'370100',青岛市:'370200',淄博市:'370300',枣庄市:'370400',东营市:'370500',烟台市:'370600',潍坊市:'370700',济宁市:'370800',泰安市:'370900',威海市:'371000',日照市:'371100',临沂市:'371300',德州市:'371400',聊城市:'371500',滨州市:'371600',菏泽市:'371700',河南省:'410000',郑州市:'410100',开封市:'410200',洛阳市:'410300',平顶山市:'410400',安阳市:'410500',鹤壁市:'410600',新乡市:'410700',焦作市:'410800',濮阳市:'410900',许昌市:'411000',漯河市:'411100',三门峡市:'411200',南阳市:'411300',商丘市:'411400',信阳市:'411500',周口市:'411600',驻马店市:'411700',湖北省:'420000',武汉市:'420100',黄石市:'420200',十堰市:'420300',宜昌市:'420500',襄阳市:'420600',鄂州市:'420700',荆门市:'420800',孝感市:'420900',荆州市:'421000',黄冈市:'421100',咸宁市:'421200',随州市:'421300',恩施土家族苗族自治州:'422800',湖南省:'430000',长沙市:'430100',株洲市:'430200',湘潭市:'430300',衡阳市:'430400',邵阳市:'430500',岳阳市:'430600',常德市:'430700',张家界市:'430800',益阳市:'430900',郴州市:'431000',永州市:'431100',怀化市:'431200',娄底市:'431300',湘西土家族苗族自治州:'433100',广东省:'440000',广州市:'440100',韶关市:'440200',深圳市:'440300',珠海市:'440400',汕头市:'440500',佛山市:'440600',江门市:'440700',湛江市:'440800',茂名市:'440900',肇庆市:'441200',惠州市:'441300',梅州市:'441400',汕尾市:'441500',河源市:'441600',阳江市:'441700',清远市:'441800',东莞市:'441900',中山市:'442000',潮州市:'445100',揭阳市:'445200',云浮市:'445300',广西壮族自治区:'450000',南宁市:'450100',柳州市:'450200',桂林市:'450300',梧州市:'450400',北海市:'450500',防城港市:'450600',钦州市:'450700',贵港市:'450800',玉林市:'450900',百色市:'451000',贺州市:'451100',河池市:'451200',来宾市:'451300',崇左市:'451400',海南省:'460000',海口市:'460100',三亚市:'460200',三沙市:'460300',儋州市:'460400',重庆市:'500000',四川省:'510000',成都市:'510100',自贡市:'510300',攀枝花市:'510400',泸州市:'510500',德阳市:'510600',绵阳市:'510700',广元市:'510800',遂宁市:'510900',内江市:'511000',乐山市:'511100',南充市:'511300',眉山市:'511400',宜宾市:'511500',广安市:'511600',达州市:'511700',雅安市:'511800',巴中市:'511900',资阳市:'512000',阿坝藏族羌族自治州:'513200',甘孜藏族自治州:'513300',凉山彝族自治州:'513400',贵州省:'520000',贵阳市:'520100',六盘水市:'520200',遵义市:'520300',安顺市:'520400',毕节市:'520500',铜仁市:'520600',黔西南布依族苗族自治州:'522300',黔东南苗族侗族自治州:'522600',黔南布依族苗族自治州:'522700',云南省:'530000',昆明市:'530100',曲靖市:'530300',玉溪市:'530400',保山市:'530500',昭通市:'530600',丽江市:'530700',普洱市:'530800',临沧市:'530900',楚雄彝族自治州:'532300',红河哈尼族彝族自治州:'532500',文山壮族苗族自治州:'532600',西双版纳傣族自治州:'532800',大理白族自治州:'532900',德宏傣族景颇族自治州:'533100',怒江傈僳族自治州:'533300',迪庆藏族自治州:'533400',西藏自治区:'540000',拉萨市:'540100',日喀则市:'540200',昌都市:'540300',林芝市:'540400',山南市:'540500',那曲市:'540600',阿里地区:'542500',陕西省:'610000',西安市:'610100',铜川市:'610200',宝鸡市:'610300',咸阳市:'610400',渭南市:'610500',延安市:'610600',汉中市:'610700',榆林市:'610800',安康市:'610900',商洛市:'611000',甘肃省:'620000',兰州市:'620100',嘉峪关市:'620200',金昌市:'620300',白银市:'620400',天水市:'620500',武威市:'620600',张掖市:'620700',平凉市:'620800',酒泉市:'620900',庆阳市:'621000',定西市:'621100',陇南市:'621200',临夏回族自治州:'622900',甘南藏族自治州:'623000',青海省:'630000',西宁市:'630100',海东市:'630200',海北藏族自治州:'632200',黄南藏族自治州:'632300',海南藏族自治州:'632500',果洛藏族自治州:'632600',玉树藏族自治州:'632700',海西蒙古族藏族自治州:'632800',宁夏回族自治区:'640000',银川市:'640100',石嘴山市:'640200',吴忠市:'640300',固原市:'640400',中卫市:'640500',新疆维吾尔自治区:'650000',乌鲁木齐市:'650100',克拉玛依市:'650200',吐鲁番市:'650400',哈密市:'650500',昌吉回族自治州:'652300',博尔塔拉蒙古自治州:'652700',巴音郭楞蒙古自治州:'652800',阿克苏地区:'652900',克孜勒苏柯尔克孜自治州:'653000',喀什地区:'653100',和田地区:'653200',伊犁哈萨克自治州:'654000',塔城地区:'654200',阿勒泰地区:'654300',台湾省:'710000',香港特别行政区:'810000',澳门特别行政区:'820000'}
    const myChart0 = echarts.init(document.getElementById('chart'))
    GetMapJson('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')

    document.getElementById('back').addEventListener('click', function () {
        GetMapJson('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')
    })



    function GetMapJson (url) {
        const  httpRequest = new XMLHttpRequest() // 第一步：建立所需的对象
        httpRequest.open('GET', url, true) // 第二步：打开连接  将请求参数写在url中  ps:"./Ptest.php?name=test&nameone=testone"
        httpRequest.send() // 第三步：发送请求  将请求参数写在URL中
        httpRequest.onreadystatechange = function () {
            if (httpRequest.readyState == 4 && httpRequest.status == 200) {
                const mapJson = JSON.parse(httpRequest.responseText)
                echarts.registerMap('map', mapJson)

                if (myChart0.value !== null && myChart0.value !== undefined) {
                    myChart0.value.dispose() // 销毁
                }
                myChart0.setOption(mapOption)
                myChart0.on('click', params => {
                    if (adcode[params.name] !== undefined) {
                        GetMapJson(`https://geo.datav.aliyun.com/areas_v3/bound/${adcode[params.name]}_full.json`)
                    }
                })
            }
        }
        return undefined
    }
	*/
}