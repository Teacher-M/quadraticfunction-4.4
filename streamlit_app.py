import streamlit as st


st.set_page_config(
    page_title="이차함수 y=ax²+q 탐구",
    page_icon="📈",
    layout="wide"
)

st.title("📈 이차함수 y = ax² + q의 그래프 탐구")

st.write(
    "q의 값을 바꾸면서 y = ax²의 그래프와 비교해 보고, "
    "그래프가 어떻게 달라지는지 관찰해 보세요."
)

st.info(
    "그래프를 관찰하면서 q의 값에 따라 "
    "어떤 변화가 나타나는지 찾아보세요."
)


# ==================================================
# 함수 이름
# ==================================================

def function_name(a, q):

    if a == 1:
        base = "x²"

    elif a == -1:
        base = "-x²"

    else:
        base = f"{a}x²"

    if q == 0:
        return f"y = {base}"

    elif q > 0:
        return f"y = {base} + {q}"

    else:
        return f"y = {base} - {abs(q)}"


# ==================================================
# 그래프 데이터 만들기
# ==================================================

def make_graph_rows(functions, x_min, x_max):

    rows = []

    # 0.05 간격
    start = int(x_min * 20)
    end = int(x_max * 20)

    for i in range(start, end + 1):

        x = i / 20

        for a, q in functions:

            rows.append(
                {
                    "x": x,
                    "y": a * x**2 + q,
                    "함수": function_name(a, q)
                }
            )

    return rows


# ==================================================
# 그래프 그리기
# ==================================================

def draw_graph(
    functions,
    x_domain,
    y_domain,
    graph_key,
    width=720,
    height=500
):

    rows = make_graph_rows(
        functions=functions,
        x_min=x_domain[0],
        x_max=x_domain[1]
    )

    # --------------------------------------------------
    # x축 정수 눈금
    # --------------------------------------------------

    x_ticks = list(
        range(
            int(x_domain[0]),
            int(x_domain[1]) + 1
        )
    )


    # --------------------------------------------------
    # y축 1단위 눈금
    # --------------------------------------------------

    y_ticks = list(
        range(
            int(y_domain[0]),
            int(y_domain[1]) + 1
        )
    )


    # y축 가로 격자선 데이터
    y_grid_rows = [
        {"y": y}
        for y in y_ticks
    ]


    # y축 숫자를 직접 표시하기 위한 데이터
    y_label_rows = [
        {
            "x": x_domain[0] + 0.12,
            "y": y,
            "label": str(y)
        }
        for y in y_ticks
    ]


    chart = {

        "width": width,
        "height": height,

        "layer": [

            # ==================================================
            # 1. y축 1단위 가로 격자선
            # ==================================================

            {
                "data": {
                    "values": y_grid_rows
                },

                "mark": {
                    "type": "rule",
                    "color": "#dddddd",
                    "strokeWidth": 1
                },

                "encoding": {

                    "y": {
                        "field": "y",
                        "type": "quantitative",

                        "scale": {
                            "domain": y_domain,
                            "nice": False
                        }
                    }
                }
            },


            # ==================================================
            # 2. 함수 그래프
            # ==================================================

            {
                "data": {
                    "values": rows
                },

                "mark": {
                    "type": "line",
                    "strokeWidth": 3,
                    "clip": True
                },

                "encoding": {

                    "x": {
                        "field": "x",
                        "type": "quantitative",

                        "scale": {
                            "domain": x_domain,
                            "nice": False
                        },

                        "axis": {
                            "title": "x",
                            "grid": True,
                            "values": x_ticks,
                            "labelFontSize": 11
                        }
                    },


                    "y": {
                        "field": "y",
                        "type": "quantitative",

                        "scale": {
                            "domain": y_domain,
                            "nice": False
                        },

                        # Vega-Lite 자동 y축 숫자는 숨김
                        "axis": {
                            "title": "y",
                            "labels": False,
                            "ticks": False,
                            "grid": False
                        }
                    },


                    "color": {
                        "field": "함수",
                        "type": "nominal",

                        "legend": {
                            "title": "함수"
                        }
                    },


                    "tooltip": [

                        {
                            "field": "함수",
                            "type": "nominal",
                            "title": "함수"
                        },

                        {
                            "field": "x",
                            "type": "quantitative",
                            "title": "x",
                            "format": ".2f"
                        },

                        {
                            "field": "y",
                            "type": "quantitative",
                            "title": "y",
                            "format": ".2f"
                        }
                    ]
                }
            },


            # ==================================================
            # 3. y축 숫자를 1단위로 직접 표시
            # ==================================================

            {
                "data": {
                    "values": y_label_rows
                },

                "mark": {
                    "type": "text",
                    "align": "left",
                    "baseline": "middle",
                    "fontSize": 11,
                    "color": "#555555"
                },

                "encoding": {

                    "x": {
                        "field": "x",
                        "type": "quantitative",

                        "scale": {
                            "domain": x_domain,
                            "nice": False
                        },

                        "axis": None
                    },

                    "y": {
                        "field": "y",
                        "type": "quantitative",

                        "scale": {
                            "domain": y_domain,
                            "nice": False
                        },

                        "axis": None
                    },

                    "text": {
                        "field": "label",
                        "type": "nominal"
                    }
                }
            },


            # ==================================================
            # 4. x축 강조
            # ==================================================

            {
                "data": {
                    "values": [
                        {"y": 0}
                    ]
                },

                "mark": {
                    "type": "rule",
                    "color": "black",
                    "strokeWidth": 2
                },

                "encoding": {

                    "y": {
                        "field": "y",
                        "type": "quantitative",

                        "scale": {
                            "domain": y_domain,
                            "nice": False
                        }
                    }
                }
            },


            # ==================================================
            # 5. y축 강조
            # ==================================================

            {
                "data": {
                    "values": [
                        {"x": 0}
                    ]
                },

                "mark": {
                    "type": "rule",
                    "color": "black",
                    "strokeWidth": 2
                },

                "encoding": {

                    "x": {
                        "field": "x",
                        "type": "quantitative",

                        "scale": {
                            "domain": x_domain,
                            "nice": False
                        }
                    }
                }
            }
        ],


        # ==================================================
        # 전체 디자인
        # ==================================================

        "config": {

            "view": {
                "stroke": "#cccccc"
            },

            "axis": {
                "titleFontSize": 15,
                "labelFontSize": 11
            },

            "legend": {
                "labelFontSize": 12,
                "titleFontSize": 13
            }
        }
    }


    value_key = "_".join(
        f"{a}_{q}"
        for a, q in functions
    )


    st.vega_lite_chart(
        chart,
        use_container_width=False,
        key=f"{graph_key}_{value_key}"
    )


# ==================================================
# 탐구 1
# ==================================================

st.divider()

st.header("탐구 1. y = x²와 y = x² + q 비교")

st.write(
    "y = x²의 그래프와 비교하면서 "
    "q의 값을 바꾸어 보세요."
)


q1 = st.slider(
    "q의 값",
    min_value=-5,
    max_value=5,
    value=2,
    step=1,
    key="q1"
)


if q1 == 0:

    compare_values_1 = [
        (1, 0)
    ]

else:

    compare_values_1 = [
        (1, 0),
        (1, q1)
    ]


draw_graph(
    functions=compare_values_1,

    x_domain=[-5, 5],
    y_domain=[-6, 16],

    graph_key="explore1"
)


st.info(
    "💭 두 그래프를 비교하여 발견한 내용을 찾아보세요."
)


# ==================================================
# 탐구 2
# ==================================================

st.divider()

st.header("탐구 2. 여러 q에 따른 그래프 비교")

st.write(
    "q의 값이 서로 다른 여러 그래프를 "
    "한 좌표평면에서 비교해 보세요."
)


draw_graph(
    functions=[
        (1, -4),
        (1, -2),
        (1, 0),
        (1, 2),
        (1, 4)
    ],

    x_domain=[-5, 5],
    y_domain=[-6, 16],

    graph_key="explore2"
)


st.info(
    "💭 여러 그래프를 비교하여 규칙을 찾아보세요."
)


# ==================================================
# 탐구 3
# ==================================================

st.divider()

st.header("탐구 3. y = ax²와 y = ax² + q 비교")

st.write(
    "a와 q의 값을 바꾸면서 "
    "두 그래프를 비교해 보세요."
)


col1, col2 = st.columns(2)


with col1:

    a3 = st.slider(
        "a의 값",
        min_value=-4,
        max_value=4,
        value=2,
        step=1,
        key="a3"
    )


with col2:

    q3 = st.slider(
        "q의 값",
        min_value=-5,
        max_value=5,
        value=3,
        step=1,
        key="q3"
    )


if a3 == 0:

    st.warning(
        "a가 0이면 이차함수가 아닙니다. "
        "0이 아닌 값을 선택하세요."
    )


else:

    if q3 == 0:

        compare_values_3 = [
            (a3, 0)
        ]

    else:

        compare_values_3 = [
            (a3, 0),
            (a3, q3)
        ]


    if a3 > 0:

        y_range_3 = [
            -6,
            22
        ]

    else:

        y_range_3 = [
            -22,
            6
        ]


    draw_graph(
        functions=compare_values_3,

        x_domain=[-5, 5],
        y_domain=y_range_3,

        graph_key="explore3"
    )


    st.info(
        "💭 a가 달라져도 두 그래프 사이에서 "
        "비슷한 관계가 나타나는지 살펴보세요."
    )


# ==================================================
# 탐구 4
# ==================================================

st.divider()

st.header("탐구 4. q의 값과 그래프의 위치")

st.write(
    "q의 값을 바꾸면서 "
    "그래프가 어떻게 달라지는지 관찰해 보세요."
)


q4 = st.slider(
    "q의 값",
    min_value=-5,
    max_value=5,
    value=2,
    step=1,
    key="q4"
)


draw_graph(
    functions=[
        (1, q4)
    ],

    x_domain=[-5, 5],
    y_domain=[-6, 16],

    graph_key="explore4"
)


st.info(
    "💭 그래프에서 변하는 것과 변하지 않는 것을 찾아보세요."
)


# ==================================================
# 마무리
# ==================================================

st.divider()

st.caption(
    "※ 그래프에서 발견한 규칙을 활동지에 정리해 보세요."
)