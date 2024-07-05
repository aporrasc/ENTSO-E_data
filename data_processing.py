import pandas as pd
import dill

def create_capacity_file(cap_dict : dict) -> pd.DataFrame:
    # Aligning Technologies
    map_tech = {'Biomass':'bioST', 'Fossil Hard coal':'SCPC', 'Fossil Oil':'oil-eng', 'Fossil Peat':'SCPC', 'Hydro Run-of-river and poundage':'hydro_turbine', 'Hydro Water Reservoir':'hydro_turbine', 'Nuclear':'nuclear-3', 'Fossil Brown coal/Lignite':'SCPC', 'Fossil Coal-derived gas':'SCPC', 'Fossil Gas':'CCGT', 'Fossil Oil shale':'oil-eng', 'Geothermal':'geothermal', 'Waste':'wasteST'}
    map_df = pd.DataFrame(map_tech.values(),index=map_tech.keys(),columns=["mopo"])
    cap_df = pd.DataFrame(0,index=cap_dict.keys(),columns=list(set(list(map_tech.values()))) )
    for CC in cap_dict:
        for tech_type,capacity in zip(cap_dict[CC].columns,cap_dict[CC].to_numpy().flatten()):
            if tech_type in map_tech:
                cap_df.loc[CC,map_tech[tech_type]] += capacity
    return cap_df


def main():
    with open('data_requested.dill', 'rb') as file:
        info = dill.load(file) 

    # capacity processing
    cap_df = create_capacity_file(info["capacity"])
    cap_df.to_csv("existing_units.csv")

    # load processing

if __name__ == "__main__":
    main()