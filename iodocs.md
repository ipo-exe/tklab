# I/O documentation
 - [Imported files](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#imported-files)
 - [Output files](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#output-files)

# Imported files
These files must be prepared and sourced by the user. Samples are provided for proper formatting.

|File | Source | Format | Sample|
|:--- | :--- | :--- | :---|
|[param_lulc.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#param_lulctxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/param_lulc.txt)|
|[param_soils.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#param_soilstxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/param_soils.txt)|
|[param_hydro.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#param_hydrotxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/param_hydro.txt)|
|[map_soils.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_soilsasc) | imported by user | Raster Map | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/map_soils.asc)|
|[map_lulc.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_lulcasc) | imported by user | Raster Map | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/map_lulc.asc)|
|[map_basin.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_basinasc) | imported by user | Raster Map | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/map_basin.asc)|
|[map_twi.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_twiasc) | imported by user | Raster Map | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/map_twi.asc)|
|[map_hand.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_handasc) | imported by user | Raster Map | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/map_hand.asc)|
|[map_slope.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_slopeasc) | imported by user | Raster Map | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/map_slope.asc)|
|[map_ET_obs_Date.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_ET_obs_Dateasc) | imported by user | Raster Map | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/map_ET_obs_Date.asc)|
|[series_obs.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#series_obstxt) | imported by user | Time Series | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/series_obs.txt)|

## `param_lulc.txt`
 - **Description**: Table of LULC parameters;
 - **Source**: imported by user;
 - **Format**: Data Table;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` Color ` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | -|
|` f_cpmax ` | positive real number | spatial factor for the `cpmax` parameter | unitless|
|` f_sfmax ` | positive real number | spatial factor for the `sfmax` parameter | unitless|
|` f_roots ` | positive real number | spatial factor for the `roots` parameter | unitless|
|` f_perv ` | positive real number | spatial factor of perviousness(1 = 100% pervious) | unitless|
|` usle_C ` | positive real number | USLE `C` parameter | unitless|
|` usle_P ` | positive real number | USLE `P` parameter | unitless|
|` load_N ` | positive real number | Effective annual Nitrogen load | kgN / yr|
|` load_P` | positive real number | Effective annual Phosphorous load | kgP / yr|
 - **File sample**: [param_lulc.txt](https://github.com/ipo-exe/tklab/blob/main/samples/param_lulc.txt);
 - **Formating example**:
```
Id;     Name;   Alias;   Color;  f_cpmax;  f_sfmax;  f_rzd
 1;    Water;      Wt;    blue;      1.0;      1.0;    1.0
 2;    Crops;      Cr;     red;      1.1;      1.3;    1.2
 3;   Forest;      Fr;   green;      1.9;      1.5;    2.0
```
## `param_soils.txt`
 - **Description**: Table of Soils parameters;
 - **Source**: imported by user;
 - **Format**: Data Table;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` Color ` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | -|
|` f_ksat ` | positive real number | spatial factor for the `ksat` parameter | unitless|
|` f_rho ` | positive real number | spatial factor for the `rho` parameter | unitless|
|` usle_K` | positive real number | USLE `K` parameter | ton h / (MJ mm)|
 - **File sample**: [param_soils.txt](https://github.com/ipo-exe/tklab/blob/main/samples/param_soils.txt);
 - **Formating example**:

## `param_hydro.txt`
 - **Description**: Table of model parameters;
 - **Source**: imported by user;
 - **Format**: Data Table;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Parameter ` | text | Parameter name | -|
|` Set ` | positive real number | Set value of parameter | -|
|` Min ` | positive real number | Minimum value of parameter in confidence interval | -|
|` Max` | positive real number | Maximum value of parameter in confidence interval | -|
 - **File sample**: [param_hydro.txt](https://github.com/ipo-exe/tklab/blob/main/samples/param_hydro.txt);
 - **Formating example**:

## `map_soils.asc`
 - **Description**: Map of Soils types;
 - **Source**: imported by user;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_soils.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_soils.asc);
 - **Formating example**:

## `map_lulc.asc`
 - **Description**: Map of LULC (land use and land cover) classes;
 - **Source**: imported by user;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_lulc.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_lulc.asc);
 - **Formating example**:

## `map_basin.asc`
 - **Description**: Basin boolean map;
 - **Source**: imported by user;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_basin.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_basin.asc);
 - **Formating example**:

## `map_twi.asc`
 - **Description**: Map of the Topographical Wetness Index (TWI);
 - **Source**: imported by user;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_twi.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_twi.asc);
 - **Formating example**:

## `map_hand.asc`
 - **Description**: Map of the Height Above Nearest Drainage (HAND);
 - **Source**: imported by user;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_hand.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_hand.asc);
 - **Formating example**:

## `map_slope.asc`
 - **Description**: Map of terrain slope;
 - **Source**: imported by user;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_slope.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_slope.asc);
 - **Formating example**:

## `map_ET_obs_Date.asc`
 - **Description**: Map of observed Evapotranspiration in Date={Date};
 - **Source**: imported by user;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_ET_obs_Date.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_ET_obs_Date.asc);
 - **Formating example**:

## `series_obs.txt`
 - **Description**: Time series of observed hydrologic processes;
 - **Source**: imported by user;
 - **Format**: Time Series;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
	 - Time resolution: daily timesteps;
	 - Date format: `YYYY-MM-DD`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Date ` | date | Date of record | -|
|` P ` | positive real number | Precipitation | mm/d|
|` T ` | positive real number | Mean daily temperature | Celcius|
|` IRA ` | positive real number | Irrigation by aspersion | mm/d|
|` IRI` | positive real number | Irrigation by inundation or dripping | mm/d|
 - **Optional Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Q_obs ` | positive real number | Observed specific streamflow | mm/d|
|` Flow_obs ` | positive real number | Observed streamflow | m3/s|
|` ET_obs ` | positive real number | Observed Evapotranspiration  | mm/d|
|` f_cpmax_Alias ` | positive real number | temporal factor for the `cpmax` parameter for LULC types (ex: `f_cpmax_Fs` |  where `Fs` is the LULC Alias for `Forest`)|
|` f_sfmax_Alias ` | positive real number | temporal factor for the `sfmax` parameter for LULC types (ex: `f_sfmax_Fs` |  where `Fs` is the LULC Alias for `Forest`)|
|` f_roots_Alias` | positive real number | temporal factor for the `roots` parameter for LULC types (ex: `f_roots_Fs` |  where `Fs` is the LULC Alias for `Forest`)|
 - **File sample**: [series_obs.txt](https://github.com/ipo-exe/tklab/blob/main/samples/series_obs.txt);
 - **Formating example**:
```
      Date;     P;     T; IRA; IRI;  Qobs; FlowObs
2011-01-01;   0.0; 24.94; 0.0; 0.0; 0.251;   2.483
2011-01-02;  15.7; 23.44; 0.0; 0.0; 0.238;   2.361
2011-01-03;  8.15; 24.04; 0.0; 0.0; 0.204;   2.018
2011-01-04;   0.0; 25.64; 2.0; 0.0; 0.154;   1.522
2011-01-05;   0.0;  26.8; 0.0; 0.0; 0.128;   1.268
2011-01-06; 27.95; 27.12; 0.0; 3.0; 1.043;  10.322
2011-01-07;  8.95; 27.64; 0.0; 0.0; 0.873;    8.64
```
# Output files
These files are generated by the program. Note that the user may source it as input to other processes.

|File | Source | Format|
|:--- | :--- | :---|
|[param_shru.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#param_shrutxt) | process output | Data Table|
|[hist2d_extent.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#hist2d_extenttxt) | process output | Data Table|
|[hist2d_basin.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#hist2d_basintxt) | process output | Data Table|
|[zmap_Var_Date.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#zmap_Var_Datetxt) | process output | Data Table|
|[zmap_Var_Stat.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#zmap_Var_Stattxt) | process output | Data Table|
|[zmap_Var_Stat_annual.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#zmap_Var_Stat_annualtxt) | process output | Data Table|
|[map_shru.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_shruasc) | process output | Raster Map|
|[map_Var_Date.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_Var_Dateasc) | process output | Raster Map|
|[map_Var_Stat.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_Var_Statasc) | process output | Raster Map|
|[map_Var_annual_Stat.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_Var_annual_Statasc) | process output | Raster Map|
|[series_sim.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#series_simtxt) | process output | Time Series|

## `param_shru.txt`
 - **Description**: Table of SHRU parameters;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` f_cpmax ` | positive real number | spatial factor for the `cpmax` parameter | unitless|
|` f_sfmax ` | positive real number | spatial factor for the `sfmax` parameter | unitless|
|` f_roots ` | positive real number | spatial factor for the `roots` parameter | unitless|
|` f_perv ` | positive real number | spatial factor of perviousness(1 = 100% pervious) | unitless|
|` usle_C ` | positive real number | USLE `C` parameter | unitless|
|` usle_P ` | positive real number | USLE `P` parameter | unitless|
|` load_N ` | positive real number | Effective annual Nitrogen load | kgN / yr|
|` load_P ` | positive real number | Effective annual Phosphorous load | kgP / yr|
|`  f_ksat ` | positive real number | spatial factor for the `ksat` parameter | unitless|
|` f_rho ` | positive real number | spatial factor for the `rho` parameter | unitless|
|` usle_K` | positive real number | USLE `K` parameter | ton h / (MJ mm)|
 - **File sample**: [param_shru.txt](https://github.com/ipo-exe/tklab/blob/main/samples/param_shru.txt);
 - **Formating example**:

## `hist2d_extent.txt`
 - **Description**: 2-D histogram (counting matrix) of spatial units within the full map extent;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **File sample**: [hist2d_extent.txt](https://github.com/ipo-exe/tklab/blob/main/samples/hist2d_extent.txt);
 - **Formating example**:

## `hist2d_basin.txt`
 - **Description**: 2-D histogram (counting matrix) of spatial units within the basin extent;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **File sample**: [hist2d_basin.txt](https://github.com/ipo-exe/tklab/blob/main/samples/hist2d_basin.txt);
 - **Formating example**:

## `zmap_Var_Date.txt`
 - **Description**: ZMap of simulated Var={Var} in Date={Date} (ex: zmap_Inf_2022-02-01);
 - **Source**: process output;
 - **Format**: Data Table;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **File sample**: [zmap_Var_Date.txt](https://github.com/ipo-exe/tklab/blob/main/samples/zmap_Var_Date.txt);
 - **Formating example**:

## `zmap_Var_Stat.txt`
 - **Description**: ZMap of the statistics Stat={Stat} of simulated Var={Var} (ex: zmap_Inf_Sum);
 - **Source**: process output;
 - **Format**: Data Table;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **File sample**: [zmap_Var_Stat.txt](https://github.com/ipo-exe/tklab/blob/main/samples/zmap_Var_Stat.txt);
 - **Formating example**:

## `zmap_Var_Stat_annual.txt`
 - **Description**: ZMap of the statistics Stat={Stat} of simulated Var={Var} in annual scale (ex: zmap_Inf_Sum_annual);
 - **Source**: process output;
 - **Format**: Data Table;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **File sample**: [zmap_Var_Stat_annual.txt](https://github.com/ipo-exe/tklab/blob/main/samples/zmap_Var_Stat_annual.txt);
 - **Formating example**:

## `map_shru.asc`
 - **Description**: Map of SHRU (surface hydrologic response units);
 - **Source**: process output;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_shru.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_shru.asc);
 - **Formating example**:

## `map_Var_Date.asc`
 - **Description**: Map of simulated Var={Var} in Date={Date} (ex: map_Inf_2022-02-01);
 - **Source**: process output;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_Var_Date.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_Var_Date.asc);
 - **Formating example**:

## `map_Var_Stat.asc`
 - **Description**: Map of the statistics Stat={Stat} of simulated Var={Var} (ex: map_Inf_Sum);
 - **Source**: process output;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_Var_Stat.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_Var_Stat.asc);
 - **Formating example**:

## `map_Var_annual_Stat.asc`
 - **Description**: Map of the statistics Stat={Stat} of simulated Var={Var} in annual scale (ex: map_Inf_Sum_annual);
 - **Source**: process output;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_Var_annual_Stat.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_Var_annual_Stat.asc);
 - **Formating example**:

## `series_sim.txt`
 - **Description**: Time series of simulated hydrologic processes;
 - **Source**: process output;
 - **Format**: Time Series;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
	 - Time resolution: daily timesteps;
	 - Date format: `YYYY-MM-DD`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`P ` | positive real number | Precipitation | mm/d|
|` T ` | positive real number | Mean daily temperature | Celcius|
|` IRA ` | positive real number | Irrigation by aspersion | mm/d|
|` IRI ` | positive real number | Irrigation by inundation or dripping | mm/d|
|` PET ` | positive real number | Potential evapotranspiration | mm/d|
|` ET ` | positive real number | Evapotranspiration  | mm/d|
|` Cp ` | positive real number | Canopy water stock | mm|
|` Sf ` | positive real number | Surface water stock | mm|
|` D ` | positive real number | Soil water deficit | mm|
|` Vz ` | positive real number | Vadose zone water stock | mm|
|` Inf ` | positive real number | Infiltration | mm/d|
|` Intc ` | positive real number | Interception in canopy | mm/d|
|` Ints ` | positive real number | Interception in surface | mm/d|
|` TF ` | positive real number | Throughfall (effective precipitation) | mm/d|
|` R ` | positive real number | Runoff | mm/d|
|` RIE ` | positive real number | Runoff by infiltration excess (Hortonian) | mm/d|
|` RSE ` | positive real number | Runoff by saturation excess (Dunnean) | mm/d|
|` RC ` | positive real number | Runoff coeficient (100 * R/P) | %|
|` Qv ` | positive real number | Recharge | mm/d|
|` Qs ` | positive real number | Stormflow (specific) | mm/d|
|` Qb ` | positive real number | Baseflow (specific) | mm/d|
|` Q ` | positive real number | Streamflow (specific) | mm/d|
|` Flow` | positive real number | Streamflow | m3/s|
 - **Optional Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Q_obs ` | positive real number | Observed specific streamflow | mm/d|
|` Flow_obs ` | positive real number | Observed streamflow | m3/s|
|` ET_obs ` | positive real number | Observed Evapotranspiration  | mm/d|
|` f_cpmax_Alias ` | positive real number | temporal factor for the `cpmax` parameter for LULC types (ex: `f_cpmax_Fs` |  where `Fs` is the LULC Alias for `Forest`)|
|` f_sfmax_Alias ` | positive real number | temporal factor for the `sfmax` parameter for LULC types (ex: `f_sfmax_Fs` |  where `Fs` is the LULC Alias for `Forest`)|
|` f_roots_Alias` | positive real number | temporal factor for the `roots` parameter for LULC types (ex: `f_roots_Fs` |  where `Fs` is the LULC Alias for `Forest`)|
 - **File sample**: [series_sim.txt](https://github.com/ipo-exe/tklab/blob/main/samples/series_sim.txt);
 - **Formating example**:
