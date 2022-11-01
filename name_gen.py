import random
import streamlit as st

st.title("Geospatial Name Generator:")

#names that fit in the first word
first = ('geo','digital','quantum','spatial','terra','flight','imagery','sciences','environmental','research','one','air','maps','blue','sky','carto','labs','civic','eco','hub','site','map','box','max','open','data','survey','pic','sat','space','voxel','world','location','intelligence','space','intelli','plex','GIS','sensing','systems','agro','shape','analytics','green','motion','point cloud','global','planet','hydro','evo','aerial','carta','carto','AI','3D','4D','metaverse','super','climate','land','topo','spectrum','white','black','raster','co-op','vision','cloud','scape','agro')
#names that fit in the last word
last = ('geo','digital','quantum','spatial','terra','flight','imagery','sciences','environmental','research','one','air','maps','blue','sky','carto','labs','civic','eco','hub','site','map','box','max','open','data','survey','pic','sat','space','voxel','world','location','intelligence','space','plex','GIS','matic','sensing','systems','agro','eo','shape','analytics','green','motion','point cloud','sense','global','planet','hydro','aerial','carta','carto','AI','Labs','3D','4D','metaverse','super','.io','climate','land','topo','spectrum','white','black','raster','co-op','vision','cloud','scape','agro')
#occassional last result
endcap = ('Systems', 'Labs', 'group', 'institute', 'analytics')

if st.button("Click me!"):
    for i in range(3):
        k = random.randint(0,4)
        if k != 4:
            first_name = random.choice(first)
            last_name = random.choice(last)
            while (True):
                if (first_name != last_name):
                    break  
                else: 
                    first_name = random.choice(first)
                    last_name = random.choice(last)  
            group=''.join(first_name + ' ' + last_name)
        else: 
            group=''.join(random.choice(first)+" "+ random.choice(last) + " "+ random.choice(endcap))
        st.write(group.title())
else:
    st.write("Waiting for you to click the button")
    
st.text('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀  ___
　　　　　／＞　　フ
　　　　　| 　^　 ^ l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　|　|　|
　／￣|　　 |　|　|
　| (￣ヽ＿_ヽ_)__)
　＼二つ                                                                                                                                                       
''')
