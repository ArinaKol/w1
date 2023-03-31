#import networkx as nx
import pandas as pd
import csv
from math import sqrt

from bokeh.plotting import figure, from_networkx
from bokeh.models import (BoxSelectTool, Circle, EdgesAndLinkedNodes, HoverTool,
                          MultiLine, NodesAndLinkedEdges, Plot, Range1d, TapTool)
from bokeh.models import (BoxZoomTool, Circle, HoverTool,Line,
                          MultiLine, Plot, WheelZoomTool, ResetTool)
from bokeh.palettes import Spectral4
from bokeh.layouts import column, layout, row
from bokeh.io import show, curdoc
from bokeh.models import Dropdown, Select, ColumnDataSource
from bokeh.models.callbacks import CustomJS
from bokeh.models import RadioButtonGroup, Div
import colorsys




def find_ent(gr, num):
    for n in gr.nodes():
        wt = gr.nodes[n]['id']
        if wt == num:
            return 1, n
    return 0, 0

def set_xy_ent(gr):
    print("set")
    for n in gr.nodes():
        ax=gr.nodes[n]['x']
        ay=gr.nodes[n]['y']
        ax1=0
        ay1=0
        id_ent=gr.nodes[n]['id2']
        k, id_ent=find_ent(gr,id_ent)
        if k == 1:
            ax1=gr.nodes[id_ent]['x']
            ay1=gr.nodes[id_ent]['y']
        #xx.append(ax1)
        #yy.append(ay1)
        #dist.append(sqrt((ax1-ax)*(ax1-ax)+(ay1-ay)*(ay1-ay)))
        G.nodes[id_ent]['x_ent'] = ax
        G.nodes[id_ent]['y_ent'] = ay
        G.nodes[id_ent]['distance']=sqrt((ax1-ax)*(ax1-ax)+(ay1-ay)*(ay1-ay))
    #nx.set_node_attributes(gr, xx, "x_ent")
    #nx.set_node_attributes(gr, yy, "y_ent")
    #nx.set_node_attributes(gr, dist, "distance")

    return gr

def delete_host(uri):
    uri = uri.strip('\n').split('/')
    return uri[-1]

def find_rel(gr, v_1, v_2):
    i = 0
    j = 0
    ij = -1
    for n in gr.nodes():
        wt = gr.nodes[n]['title']
        ij = ij + 1
        if wt == v_1:
            v11 = gr.nodes[n]['id']
            i = 1
        if wt == v_2:
            v22 = gr.nodes[n]['id']
            j = 1
        if j == 1 and i == 1:
            return 1, v11, v22
    return 0, 0, 0



def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb




###
#G = nx.Graph()
#with open('a.csv', encoding="utf8", newline='') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#       #G.add_node(int(row['ent1_id']), id=int(row['ent1_id']), id2=int(row['ent2_id']), pos=(float(row['x']), float(row['y'])), color = 'darkblue' if row['lang'] == 'en' else 'crimson', lang=row['lang'], title=row['ent1'] if row['lang'] == 'en' else row['ent2'], type=row['type'], x=(float(row['x'])), y=float(row['y']))
#       G.add_node(int(row['ent1_id']), id=int(row['ent1_id']), id2=int(row['ent2_id']),
#                  pos=(float(row['x']), float(row['y'])), color = 'darkblue' if row['lang'] == 'en' else 'crimson',
#                  lang=row['lang'], title=row['ent1'], type=row['type'],
#                  x=(float(row['x'])), y=float(row['y']))
#pos=nx.get_node_attributes(G, 'pos')

filename = 'seu_EN_RU_15K_V1_ent.csv'
filepath = filename
df_main = pd.read_csv(filepath)
# Create Column Data Source that will be used by the plot
source = ColumnDataSource(data=dict(x=[], y=[], ent1_id=[], ent2_id=[], ent1=[], ent2=[], lang=[], type_=[], color=[], size=[], distance=[]))

filename1 = 'seu_EN_RU_15K_V1_rel.csv'
filepath1 = filename1
df_rel = pd.read_csv(filepath1)
#print(df_rel)

data = pd.read_csv(filename1, nrows=0)
#print(data)



k=0xffb5b5
k1=0xf8b5ff
n=10
#m[]={0xffd6d6,ffd6f3}
m=0xffd6f3
m1=0xffd6d6
#for i in 1,2,3,4,5,6,7,8,9,10:
#    print(hex(m-i*(m-m1)))


df_rel1=csv.reader(filepath1)
coorx=list()
coory=list()
coorx=list()
coory=list()
with open('b.csv', encoding="utf8", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for r in reader:
        coorx1=list()
        coorx1.append(float(r['xs']))
        coorx1.append(float(r['xs1']))
        coorx.append(coorx1)
        coory1 = list()
        coory1.append(float(r['ys']))
        coory1.append(float(r['ys1']))
        coory.append(coory1)

# Create Column Data Source that will be used by the plot
source1 = ColumnDataSource(data=dict(relation=[], id1=[], id2=[], xs=[], ys=[], line=[], color=[]))


#print(list(source1.data['xs']))

#G = set_xy_ent(G)


# create graph renderer from networkx graph
#graph_renderer = from_networkx(G, pos)

#tool="lasso_select,pan,wheel_zoom,tap,save,reset, hover_nodes, hover_edges"
#tool1="lasso_select,pan,wheel_zoom,tap,save,reset"
p1 = figure(height=720, width=1280,x_range=(-100, 100), y_range=(-100, 100),
              tools="lasso_select,pan,wheel_zoom,tap,save,reset", active_scroll='wheel_zoom')
p1.add_tools(TapTool(), BoxSelectTool())
#graph_renderer.node_renderer.selection_glyph = Circle(size=5, fill_color='white')
#graph_renderer.node_renderer.selection_glyph = Circle(size=1, fill_color='white', line_alpha=0)
#graph_renderer.node_renderer.glyph = Circle(size=5, fill_color='yellow', line_alpha=0)
#graph_renderer.node_renderer.nonselection_glyph = Circle(size=100, fill_color='black', fill_alpha=0.2, line_alpha=0)
#graph_renderer.node_renderer.glyph = Circle(size=5, line_alpha=0.2)
#graph_renderer.edge_renderer.glyph = MultiLine(line_color="yellow", line_alpha=0, line_width=2)
#graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_alpha=5,line_width=20)
#graph_renderer.edge_renderer.nonselection_glyph = MultiLine(line_color='black', line_alpha=10,line_width=0)
#graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=2)

#graph_renderer.selection_policy = NodesAndLinkedEdges()
#graph_renderer.selection_policy = NodesAndLinkedEdges()
#graph_renderer.inspection_policy = NodesAndLinkedEdges()



#hover_nodes = HoverTool(
#    tooltips=[('title','@title'),('id','@id'),('type','@type'),('lang','@lang'),('x,y','@pos'),('id','@id2'),('x,y','@x_ent,@y_ent'),('distance','@distance')],renderers=[graph_renderer.node_renderer]
#)

#hover_edges = HoverTool(
#    tooltips=[('relation', '@rel')], renderers=[graph_renderer.edge_renderer]
#)
#plot.add_tools(hover_edges, hover_nodes)
#plot.renderers.append(graph_renderer)

############################################
types = list(df_main['type'].unique())
types=list(set(types))
types = sorted(types)
types.insert(0, 'All')
select_type = Select(name='select_type', title='Тип', options=types, value=types[0])

ids = list(df_main['ent1_id'])
ids = list(map(str, ids))
ids.insert(0, '-1')
select_id = Select(name='select_id', title='Номер', options=ids, value=ids[0], visible=False)


def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))


#(h,s,v)=(0,0.11,1)
#(r, g, b) = hsv2rgb(h, s, v)
#print('#'+rgb_to_hex((r, g, b)))

# Form screens
select_tools = ['pan', 'wheel_zoom', 'tap', 'reset', 'save']
tooltips = [('Entity', '@ent1' + ' (@lang)'), ('Type', '@type_')]

#p1 = figure(plot_height=720, plot_width=1280, tools=select_tools, title='Векторное пространство')
p1.toolbar.active_scroll = p1.select_one(WheelZoomTool)
#p1.add_tools(HoverTool(tooltips=tooltips))


rr=p1.circle(x='x',
          y='y',
          source=source,
          color='color',
          size='size',
          nonselection_alpha=0.5)

rr1=p1.multi_line(xs='xs',
          ys='ys',
          source=source1,
          color='color',
          line_alpha='line',
          line_width=2,
          nonselection_alpha=0
        )

p1.add_tools(HoverTool(tooltips=[('title','@ent1'),('id','@ent1_id'),('type','@type_'),('lang','@lang'),('x,y','@x,@y')], renderers=[rr]))
p1.add_tools(HoverTool(tooltips=[('relation', '@relation')], renderers=[rr1]))

template=("""
      <div class='content'>
       <div class='name_'> <b>Выбранная сущность:</b> {name} </div>
       <div class='name_'> <b>Id выбранной сущности:</b> {id} </div>
       <div class='rel'> <b>Количество отношений выбранной сущности:</b> {count}</div>
       <div class='name_1'> <b>Эквивалентная сущность(id):</b> {name_eq} </div>
       <div class='name_1'> <b>Id эквивалентнаой сущности:</b> {id1} </div>
       <div class='rel'> <b>Количество отношений эквивалентной сущности:</b> {count1}</div>
       <div class='rel'> <b>Количество эквивалентных отношений сущностей:</b> {count_}</div>
      """)
template_1=("""
      <div class='rel_'> <b>Эквивалентные отношения:</b> </div>
      """)
template1=("""
       <div >{list_}</div>
      """)
template_2=("""
       <div class='rel_'> <b>Несовпадающие отношения выбранной сущности:</b></div>
      """)
template2=("""
       <div>{list1}</div>
      """)
template_3=("""
       <div class='rel_'> <b>Несовпадающие отношения эквивалентной сущности:</b></div>
      """)
template3=("""
       <div>{list_1}</div>
      """)
# initial text
text = template.format(name = " ", name_eq = " ", id=" ", id1=" ",count=" ",count1=" ",count_=" ", percentage=2,
                   colour='#97D389')
text_1 = template_1.format(percentage=2,
                   colour='#97D389')
text1 = template1.format(list_=" ",
                   percentage=2,
                   colour='#97D389')
text_2 = template_2.format(
                   percentage=2,
                   colour='#97D389')
text2 = template2.format(list1=" ",
                   percentage=2,
                   colour='#97D389')
text_3 = template_3.format(
                   percentage=2,
                   colour='#97D389')
text3 = template3.format(list_1=" ",
                   percentage=2,
                   colour='#97D389')
div = Div(text=text)#style={'overflow-y':'scroll','height':'50px'})
div1 = Div(text=text1, style={'overflow-y':'scroll','width': '100%', "height": "100%"}, width=300, height=100)
div_1 = Div(text=text_1)
div2 = Div(text=text2, style={'overflow-y':'scroll','width': '100%', "height": "100%"}, width=300, height=100)
div_2 = Div(text=text_2)
div3 = Div(text=text3, style={'overflow-y':'scroll','width': '100%', "height": "100%"}, width=300, height=100)
div_3 = Div(text=text_3)


callback = CustomJS(args=dict(source=source), code="""
    const selector = document.getElementsByName('select_id')[0];
    const indices = source.selected.indices;
    if (indices.length !== 0) {
        selector.value = indices[0];
    } else {
        selector.value = -1;
    }
    var event = new Event('change');
    const cancelled = !selector.dispatchEvent(event);
""")
p1.js_on_event('tap', callback)

LABELS = ["Сущность", "Эквив. сущность", "Обе сущности"]

radio_button_group = RadioButtonGroup(labels=LABELS, active=0)
radio_button_group.js_on_click(CustomJS(code="""
    console.log('radio_button_group: active=' + this.active, this.toString())
"""))



def set_colors(df):
    languages = list(df['lang'])
    colors = list(map(lambda x: 'darkblue' if x == 'en' else 'crimson', languages))
    df['color'] = colors
    return df


def set_params(df,df1):
    df = set_colors(df)
    df['size'] = 5
    df['distance'] = 0
    df1['line'] = 0
    df1['color'] = 'black'
    return df,df1

def set_params1(df1):
    df1['line'] = 0
    df1['color'] = 'black'
    return df1



def get_color(index):
    color = 'darkblue'
    if index % 2 != 0:
        color = 'crimson'
    return color


def emphasize_pair(df, df_ids, id1):
    print(id1)
    row = df.loc[df['ent1_id'] == id1]
    id2 = row['ent2_id'].values[0]
    pair = [id1, id2]

    colors = list(map(lambda x: get_color(x) if x in pair else 'lightgray', df_ids))
    df['color'] = colors
    sizes = list(map(lambda x: 15 if x in pair else 5, df_ids))
    df['size'] = sizes
    return df

def get_coor_line(df1):
    r1 = df1['xs'].values
    r2 = df1['xs1'].values
    c_x = list()
    for i, j in zip(r1, r2):
        cc = list()
        cc.append(float(i))
        cc.append(float(j))
        c_x.append(cc)

    r1 = df1['ys'].values
    r2 = df1['ys1'].values
    c_y = list()
    for i, j in zip(r1, r2):
        cc = list()
        cc.append(float(i))
        cc.append(float(j))
        c_y.append(cc)
    return c_x, c_y

def sel_relat(df, df1, id1):
    row=df.loc[(df['ent1_id'] == id1)]
    id = id1
    l=row['lang'].values
    l1=row['count'].values
    id_eq=int(row['ent2_id'].values)
    if l!='en':
        id1=id_eq
        id_eq=id
    df1 = df1.loc[(df1['id1'] == id1) | (df1['id2'] == id1) | (df1['id1'] == id_eq) | (df1['id2'] == id_eq)]
    #df1 = df1.loc[(df1['id1'] == id) | (df1['id2'] == id)]
    r1 = df1['id'].values
    lin=list()
    col=dict()
    count = 330 / (int(l1) if int(l1)!=0 else 1)
    count = count/360
    #print(count)
    (h,s,v)=(0,0.11,1) #en
    (h1, s1, v1) = (0, 0.11, 0.76)
    list1=list()
    list_1=list()
    for ii in r1:
        row=df1.loc[(df1['id'] == ii)]
        i=row['id1'].values
        j=row['id2'].values
        idd=row['id'].values
        row1=row['id_eq'].values
        if row1 == -1:
            if i == id1 or j ==id1:
                col[int(idd)] = 'darkblue'

                list1.append(row['rel_vis'].values[0])
            else:
                col[int(idd)] = 'crimson'
                list_1.append(row['rel_vis'].values[0])
        else:
            if int(i) == id1 or int(j) == id1:
                (r, g, b) = hsv2rgb(h, s, v)
                col[int(idd)] = '#' + rgb_to_hex((r, g, b))
                h += count
                (r, g, b) = hsv2rgb(h1, s1, v1)
                col[int(row1)] = '#' + rgb_to_hex((r, g, b))
                h1 += count
            else:
                (r, g, b) = hsv2rgb(h1, s1, v1)
                col[int(idd)] = '#' + rgb_to_hex((r, g, b))
                h1 += count
                (r, g, b) = hsv2rgb(h, s, v)
                col[int(row1)] = '#' + rgb_to_hex((r, g, b))
                h += count
        if radio_button_group.active==2:
            lin.append(1)
        else:
            if int(i) == id or int(j) == id:
                lin.append(1)
            else:
                lin.append(0)
    df1['line'] = lin
    col1=list()
    print(col)
    for i in r1:
        if i in col:
            col1.append(col[i])

    df1['color'] = col1
    if radio_button_group.active == 2:
        df1_vis = df1.copy()
    else:
        df1_vis=df1.loc[((df1['id1'] == id) | (df1['id2'] == id))]
    if l!='en':
        lt=list_1
        list_1=list1
        list1=lt
    return df1_vis,list1,list_1


def div_kg(df, current_id, list1, list_1):
    if current_id != -1:
        row = df.loc[(df['ent1_id'] == current_id)]
        name_ = str(row['ent1'].values[0])
        name_1 = str(row['ent2'].values[0])
        id_eq = int(row['ent2_id'].values)
        count = int(row['rel_count_all'].values)
        count_ = int(row['count'].values)
        row1 = df.loc[(df['ent1_id'] == int(id_eq))]
        count1 = int(row1['rel_count_all'].values)
        list_ = row['rel_count'].values
    else:
        current_id=' '
        name_ = ' '
        name_1 = ' '
        id_eq = ' '
        count = ' '
        count_ = ' '
        count1 = ' '
        list_ = ' '
    div.text = template.format(name=name_, name_eq=name_1, id=current_id, id1=id_eq, count=count, count1=count1,
                               count_=count_, percentage=2,
                               colour='#97D389')
    div1.text = template1.format(list_=''.join(list_), width=200, height=100,
                                 percentage=2,
                                 colour='#97D389')
    div2.text = template2.format(list1=''.join(list1),
                                 percentage=2,
                                 colour='#97D389', width=200, height=100)
    div3.text = template3.format(list_1=''.join(list_1),
                                 percentage=2,
                                 colour='#97D389', width=200, height=100)


def get_data():
    current_type = select_type.value
    df = df_main.copy()
    df1 = df_rel.copy()
    list1=list()
    list_1=list()
    df, df1 = set_params(df,df1)
    if current_type != 'All':
        df = df.loc[df['type'] == current_type]

    current_id = int(select_id.value)
    df_ids = list(df['ent1_id'])
    if current_id != -1:
        if current_id < len(df_ids):
            if len(df) < len(df_main):
                current_id = df_ids[current_id]
            row = df.loc[(df['ent1_id'] == current_id)]
            if radio_button_group.active == 1:
                current_id=int(row['ent2_id'].values)
            df = emphasize_pair(df, df_ids, current_id)
            df1, list1,list_1= sel_relat(df, df1, current_id)

            #div=Div(text=text)
        else:
            source.selected.indices = []
    else:
        df1=data.copy()
        df1=set_params1(df1)
    return df, df1, current_id, list1,list_1


def update():
    print(radio_button_group.active)
    df, df1, c_id, l1,l_1= get_data()
    coorx, coory = get_coor_line(df1)
    source.data = dict(
        x=df['x'], y=df['y'],
        ent1_id=df['ent1_id'], ent2_id=df['ent2_id'],
        ent1=df['ent1'], ent2=df['ent2'],
        lang=df['lang'], type_=df['type'],
        color=df['color'], size=df['size'],
        distance=df['distance']
    )
    source1.data = dict(
        relation=df1['rel_vis'], id1=df1['id1'], id2=df1['id2'],
        xs=coorx, ys=coory, line=df1['line'], color=df1['color']
    )
    div_kg(df, c_id, l1,l_1)





# declare controls
controls = [select_type, select_id]
for control in controls:
    control.on_change('value', lambda attr, old, new: update())
    radio_button_group.on_change('active', lambda attr, old, new: update())


# set up layout
inputs = column(*controls)
rad=column(radio_button_group)
#div=column(div)
inputs = column(column(inputs, rad))
inputs=column(column(inputs, div))
inputs=column(column(inputs, div_1))
inputs=column(column(inputs, div1))
inputs=column(column(inputs, div_2))
inputs=column(column(inputs, div2))
inputs=column(column(inputs, div_3))
inputs=column(column(inputs, div3))
series = column(p1)
fields = column(row(inputs, series), sizing_mode="scale_both")

update()  # initial load of the data

curdoc().add_root(fields)
curdoc().title = filename