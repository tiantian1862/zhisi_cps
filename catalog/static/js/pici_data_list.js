//---------------------------------------------------------charts1模块1
(function () {
  var dom = document.getElementById('charts1');
    var myChart = echarts.init(dom, null, {
      renderer: 'canvas',
      useDirtyRect: false
    });
    var app = {};
    
    var option;

    const posList = [
  'left',
  'right',
  'top',
  'bottom',
  'inside',
  'insideTop',
  'insideLeft',
  'insideRight',
  'insideBottom',
  'insideTopLeft',
  'insideTopRight',
  'insideBottomLeft',
  'insideBottomRight'
];
app.configParameters = {
  rotate: {
    min: -90,
    max: 90
  },
  align: {
    options: {
      left: 'left',
      center: 'center',
      right: 'right'
    }
  },
  verticalAlign: {
    options: {
      top: 'top',
      middle: 'middle',
      bottom: 'bottom'
    }
  },
  position: {
    options: posList.reduce(function (map, pos) {
      map[pos] = pos;
      return map;
    }, {})
  },
  distance: {
    min: 0,
    max: 100
  }
};
app.config = {
  rotate: 90,
  align: 'left',
  verticalAlign: 'middle',
  position: 'insideBottom',
  distance: 15,
  onChange: function () {
    const labelOption = {
      rotate: app.config.rotate,
      align: app.config.align,
      verticalAlign: app.config.verticalAlign,
      position: app.config.position,
      distance: app.config.distance
    };
    myChart.setOption({
      series: [
        {
          label: labelOption
        },
        {
          label: labelOption
        },
        {
          label: labelOption
        },
        {
          label: labelOption
        }
      ]
    });
  }
};
const labelOption = {
  show: true,
  position: app.config.position,
  distance: app.config.distance,
  align: app.config.align,
  verticalAlign: app.config.verticalAlign,
  rotate: app.config.rotate,
  formatter: '{c}  {name|{a}}',
  fontSize: 16,
  rich: {
    name: {}
  }
};
option = {

  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {
    data: ['芙蓉王', '白沙', '梗线']
  },
  toolbox: {
    show: true,
    orient: 'vertical',
    left: 'right',
    top: 'center',
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      magicType: { show: true, type: ['line', 'bar', 'stack'] },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  xAxis: [
    {
      type: 'category',
      axisTick: { show: false },
      data: ['周一', '周二', '周三', '周四', '周五','周六']
    }
  ],
  yAxis: [
    {
      type: 'value'
    }
  ],
  series: [
    {
      name: '芙蓉王',
      type: 'bar',
      barGap: 0,
      label: labelOption,
      emphasis: {
        focus: 'series'
      },
      data: [30000, 25000, 35000, 20000, 20000,]
    },
    {
      name: '白沙',
      type: 'bar',
      label: labelOption,
      emphasis: {
        focus: 'series'
      },
      data: [36000, 28000, 17680, 23000, 5000]
    },
    {
      name: '梗线',
      type: 'bar',
      label: labelOption,
      emphasis: {
        focus: 'series'
      },
      data: [8000, 0, 4000, 4000, 2000]
    }
  ]
};
  // 3.把配置项给实例对象
  myChart.setOption(option);

  // 4.让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart.resize();
  })
})();

//---------------------------------------------------------charts1模块2
(function () {
  // 1.实例化对象
  var dom = document.getElementById('charts3');
    var myChart = echarts.init(dom, null, {
      renderer: 'canvas',
      useDirtyRect: false
    });
    var app = {};
    
    var option;

    // prettier-ignore
const data = [["04-01", 116], ["04-02", 0],["04-03", 60],["04-04", 40],["04-05", 26],["04-06", 160],["04-07", 70],["04-08", 22],["04-09", 0],["04-10", 60],["04-11", 50],["04-12", 22],["04-13", 90],["04-14", 60]];
const dateList = data.map(function (item) {
  return item[0];
});
const valueList = data.map(function (item) {
  return item[1];
});
option = {
  // Make gradient line here
  visualMap: [
    {
      show: false,
      type: 'continuous',
      seriesIndex: 0,
      min: 0,
      max: 400
    },
  ],
  title: [
    {
      left: 'center',
      text: '生产停车时间'
    },
  ],
  tooltip: {
    trigger: 'axis'
  },
  xAxis: [
    {
      data: dateList
    },
  ],
  yAxis: [
    {},
  ],
  grid: [
    {
      bottom: '60%'
    },
  ],
  series: [
    {
      type: 'line',
      showSymbol: false,
      data: valueList
    },
  ]
};
  myChart.setOption(option);
  // 4.让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart.resize();
  })
})();

//---------------------------------------------------------charts1模块3
(function () {
  // 1.实例化对象
  var dom = document.getElementById('charts2');
    var myChart = echarts.init(dom, null, {
      renderer: 'canvas',
      useDirtyRect: false
    });
    var app = {};
    
    var option;

    // prettier-ignore
let dataAxis = ['点', '击', '柱', '子', '或', '者', '两', '指', '在', '触', '屏', '上', '滑', '动', '能', '够', '自', '动', '缩', '放'];
// prettier-ignore
let data = [15, 18, 20, 10, 16, 19, 16, 18, 19, 0, 16, 19, 16, 15, 16, 17, 18, 13, 12, 10,12,11,15,0,12,13,11,12,16,5];
let yMax = 24;
let dataShadow = [];
for (let i = 0; i < data.length; i++) {
  dataShadow.push(yMax);
}
option = {
  title: {
    left:'center',
    text: '生产耗时',
    subtext: ''
  },
  xAxis: {
    data: dataAxis,
    axisLabel: {
      inside: true,
      color: '#fff'
    },
    axisTick: {
      show: false
    },
    axisLine: {
      show: false
    },
    z: 10
  },
  xAxis: {
    type: 'category',
    //boundaryGap: false, // 去除轴间距
    data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],
    // 去除刻度线
    axisTick: {
      show: false
    },
    axisLabel: {
      color: "#4c9bfb" // x轴文本颜色
    },
    axisLine: {
      show: false // 去除轴线
    },
    z: 10
  },
  yAxis: {
    axisLine: {
      show: false
    },
    axisTick: {
      show: false
    },
    axisLabel: {
      color: '#999'
    }
  },
  dataZoom: [
    {
      type: 'inside'
    }
  ],
  series: [
    {
      type: 'bar',
      showBackground: true,
      itemStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: '#83bff6' },
          { offset: 0.5, color: '#188df0' },
          { offset: 1, color: '#188df0' }
        ])
      },
      emphasis: {
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: '#2378f7' },
            { offset: 0.7, color: '#2378f7' },
            { offset: 1, color: '#83bff6' }
          ])
        }
      },
      data: data
    }
  ]
};
// Enable data zoom when user click bar.
const zoomSize = 6;
myChart.on('click', function (params) {
  console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
  myChart.dispatchAction({
    type: 'dataZoom',
    startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
    endValue:
      dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
  });
});

  myChart.setOption(option);

  // 4.让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart.resize();
  })
})();

//charts1模块4
(function () {
  // 1.实例化对象


  myChart.setOption(option);

  // 4.让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart.resize();
  })
})();
