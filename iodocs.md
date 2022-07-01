# I/O documentation
 - [Imported files](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#imported-files)
 - [Output files](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#output-files)
 - [Glossary](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#glossary)

# Imported files
These files must be prepared and sourced by the user. Samples are provided for proper formatting.

|File | Source | Format | Sample|
|:--- | :--- | :--- | :---|
|[param_lulc.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#param_lulctxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/param_lulc.txt)|
|[param_soils.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#param_soilstxt) | imported by user | Data Table | missing|
|[param_hydro.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#param_hydrotxt) | imported by user | Data Table | missing|
|[map_soils.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_soilsasc) | imported by user | Raster Map | missing|
|[map_lulc.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_lulcasc) | imported by user | Raster Map | missing|
|[map_basin.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_basinasc) | imported by user | Raster Map | missing|
|[map_twi.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_twiasc) | imported by user | Raster Map | missing|
|[map_hand.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_handasc) | imported by user | Raster Map | missing|
|[map_slope.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_slopeasc) | imported by user | Raster Map | missing|
|[map_ET_obs_Date.asc](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#map_ET_obs_Dateasc) | imported by user | Raster Map | missing|
|[series_obs.txt](https://github.com/ipo-exe/tklab/blob/main/iodocs.md#series_obstxt) | imported by user | Time Series | [Sample file](https://github.com/ipo-exe/tklab/blob/main/samples/series_obs.txt)|

## `param_lulc.txt`
 - **Description**: Table of LULC parameters;
 - **Source**: imported by user;
 - **File sample**: [param_lulc.txt](https://github.com/ipo-exe/tklab/blob/main/samples/param_lulc.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
Id;    Name; Alias;   Color; f_cpmax; f_sfmax; f_roots; f_perv; usle_C; usle_P; load_N; load_P
 1;   Water;    Wa;    blue;    0.07;    0.07;    0.07;      1;  0.001;      1;      0;      0
 2;   Urban;    Ur; #8c8a85;     0.2;     0.2;     0.2;    0.6;    0.3;      1;   4.65;  0.124
 3;  Forest;    Fs;   green;       1;       1;       1;      1;  0.001;      1;   2.19;  0.142
 4;   Crops;    Cr;     red;     0.4;     0.4;     0.4;      1;    0.4;      1; 10.768;  1.263
 5; Pasture;    Ps; #79a832;    0.53;    0.53;    0.53;      1;    0.1;      1;  1.825;  0.102
 6;   Roads;    Rd;   white;    0.07;    0.07;    0.07;    0.1;      1;      1;   4.65;  0.124
```
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
|` load_N ` | positive real number | Effective annual Nitrogen load | kgN / ha yr|
|` load_P` | positive real number | Effective annual Phosphorous load | kgP / ha yr|

## `param_soils.txt`
 - **Description**: Table of Soils parameters;
 - **Source**: imported by user;
 - **File sample**: _missing_;
 - **Format**: Data Table;
 - **Formating example**:
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

## `param_hydro.txt`
 - **Description**: Table of model parameters;
 - **Source**: imported by user;
 - **File sample**: _missing_;
 - **Format**: Data Table;
 - **Formating example**:
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

## `map_soils.asc`
 - **Description**: Map of Soils types;
 - **Source**: imported by user;
 - **File sample**: _missing_;
 - **Format**: Raster Map;
 - **Formating example**:
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;

## `map_lulc.asc`
 - **Description**: Map of LULC (land use and land cover) classes;
 - **Source**: imported by user;
 - **File sample**: _missing_;
 - **Format**: Raster Map;
 - **Formating example**:
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;

## `map_basin.asc`
 - **Description**: Basin boolean map;
 - **Source**: imported by user;
 - **File sample**: _missing_;
 - **Format**: Raster Map;
 - **Formating example**:
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;

## `map_twi.asc`
 - **Description**: Map of the Topographical Wetness Index (TWI);
 - **Source**: imported by user;
 - **File sample**: _missing_;
 - **Format**: Raster Map;
 - **Formating example**:
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;

## `map_hand.asc`
 - **Description**: Map of the Height Above Nearest Drainage (HAND);
 - **Source**: imported by user;
 - **File sample**: _missing_;
 - **Format**: Raster Map;
 - **Formating example**:
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;

## `map_slope.asc`
 - **Description**: Map of terrain slope;
 - **Source**: imported by user;
 - **File sample**: _missing_;
 - **Format**: Raster Map;
 - **Formating example**:
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;

## `map_ET_obs_Date.asc`
 - **Description**: Map of observed Evapotranspiration in Date={Date};
 - **Source**: imported by user;
 - **File sample**: _missing_;
 - **Format**: Raster Map;
 - **Formating example**:
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;

## `series_obs.txt`
 - **Description**: Time series of observed hydrologic processes;
 - **Source**: imported by user;
 - **File sample**: [series_obs.txt](https://github.com/ipo-exe/tklab/blob/main/samples/series_obs.txt);
 - **Format**: Time Series;
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
|` f_cpmax_Alias ` | positive real number | temporal factor for the `cpmax` parameter for LULC types (ex: `f_cpmax_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless|
|` f_sfmax_Alias ` | positive real number | temporal factor for the `sfmax` parameter for LULC types (ex: `f_sfmax_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless|
|` f_roots_Alias` | positive real number | temporal factor for the `roots` parameter for LULC types (ex: `f_roots_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless|

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
 - **Formating example**:
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
|` load_N ` | positive real number | Effective annual Nitrogen load | kgN / ha yr|
|` load_P ` | positive real number | Effective annual Phosphorous load | kgP / ha yr|
|`  f_ksat ` | positive real number | spatial factor for the `ksat` parameter | unitless|
|` f_rho ` | positive real number | spatial factor for the `rho` parameter | unitless|
|` usle_K` | positive real number | USLE `K` parameter | ton h / (MJ mm)|

## `hist2d_extent.txt`
 - **Description**: 2-D histogram (counting matrix) of spatial units within the full map extent;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;

## `hist2d_basin.txt`
 - **Description**: 2-D histogram (counting matrix) of spatial units within the basin extent;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;

## `zmap_Var_Date.txt`
 - **Description**: ZMap of simulated Var={Var} in Date={Date} (ex: zmap_Inf_2022-02-01);
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;

## `zmap_Var_Stat.txt`
 - **Description**: ZMap of the statistics Stat={Stat} of simulated Var={Var} (ex: zmap_Inf_Sum);
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;

## `zmap_Var_Stat_annual.txt`
 - **Description**: ZMap of the statistics Stat={Stat} of simulated Var={Var} in annual scale (ex: zmap_Inf_Sum_annual);
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;

## `map_shru.asc`
 - **Description**: Map of SHRU (surface hydrologic response units);
 - **Source**: process output;
 - **Format**: Raster Map;
 - **Formating example**:
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;

## `map_Var_Date.asc`
 - **Description**: Map of simulated Var={Var} in Date={Date} (ex: map_Inf_2022-02-01);
 - **Source**: process output;
 - **Format**: Raster Map;
 - **Formating example**:
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;

## `map_Var_Stat.asc`
 - **Description**: Map of the statistics Stat={Stat} of simulated Var={Var} (ex: map_Inf_Sum);
 - **Source**: process output;
 - **Format**: Raster Map;
 - **Formating example**:
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;

## `map_Var_annual_Stat.asc`
 - **Description**: Map of the statistics Stat={Stat} of simulated Var={Var} in annual scale (ex: map_Inf_Sum_annual);
 - **Source**: process output;
 - **Format**: Raster Map;
 - **Formating example**:
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;

## `series_sim.txt`
 - **Description**: Time series of simulated hydrologic processes;
 - **Source**: process output;
 - **Format**: Time Series;
 - **Formating example**:
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
|` f_cpmax_Alias ` | positive real number | temporal factor for the `cpmax` parameter for LULC types (ex: `f_cpmax_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless|
|` f_sfmax_Alias ` | positive real number | temporal factor for the `sfmax` parameter for LULC types (ex: `f_sfmax_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless|
|` f_roots_Alias` | positive real number | temporal factor for the `roots` parameter for LULC types (ex: `f_roots_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless|

## Glossary

### By A-Z order
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`Alias` | text | Category alias (one-word only) | - | field|
|`Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | - | field|
|`Cp` | positive real number | Canopy water stock | mm | variable|
|`D` | positive real number | Soil water deficit | mm | variable|
|`Date` | date | Date of record | - | field|
|`ET` | positive real number | Evapotranspiration  | mm/d | variable|
|`ET_obs` | positive real number | Observed Evapotranspiration  | mm/d | variable|
|`Flow` | positive real number | Streamflow | m3/s | variable|
|`Flow_obs` | positive real number | Observed streamflow | m3/s | variable|
|`IRA` | positive real number | Irrigation by aspersion | mm/d | variable|
|`IRI` | positive real number | Irrigation by inundation or dripping | mm/d | variable|
|`Id` | unique integer number | Category numerical identifyier | - | field|
|`Inf` | positive real number | Infiltration | mm/d | variable|
|`Intc` | positive real number | Interception in canopy | mm/d | variable|
|`Ints` | positive real number | Interception in surface | mm/d | variable|
|`Max` | text | Keyword for `Maximum` | - | keyword|
|`Max` | positive real number | Maximum value of parameter in confidence interval | - | field|
|`Mean` | text | Keyword for `Mean` | - | keyword|
|`Med` | text | Keyword for `Median` | - | keyword|
|`Min` | positive real number | Minimum value of parameter in confidence interval | - | field|
|`Min` | text | Keyword for `Minimum` | - | keyword|
|`Name` | text | Category name | - | field|
|`P` | positive real number | Precipitation | mm/d | variable|
|`PET` | positive real number | Potential evapotranspiration | mm/d | variable|
|`Parameter` | text | Parameter name | - | field|
|`Q` | positive real number | Streamflow (specific) | mm/d | variable|
|`Q_obs` | positive real number | Observed specific streamflow | mm/d | variable|
|`Qb` | positive real number | Baseflow (specific) | mm/d | variable|
|`Qs` | positive real number | Stormflow (specific) | mm/d | variable|
|`Qt0` | positive real number | Streamflow (specific) when t=0 (initial condition) | mm/d | parameter|
|`Qv` | positive real number | Recharge | mm/d | variable|
|`R` | positive real number | Runoff | mm/d | variable|
|`RC` | positive real number | Runoff coeficient (100 * R/P) | % | variable|
|`RIE` | positive real number | Runoff by infiltration excess (Hortonian) | mm/d | variable|
|`RSE` | positive real number | Runoff by saturation excess (Dunnean) | mm/d | variable|
|`SD` | text | Keyword for `Standard Deviation` | - | keyword|
|`Set` | positive real number | Set value of parameter | - | field|
|`Sf` | positive real number | Surface water stock | mm | variable|
|`Stat` | text | Keyword for `statistic` | - | keyword|
|`Sum` | text | Keyword for `sum` | - | keyword|
|`T` | positive real number | Mean daily temperature | Celcius | variable|
|`TF` | positive real number | Throughfall (effective precipitation) | mm/d | variable|
|`Var` | text | Keyword for `variable` | - | keyword|
|`Vz` | positive real number | Vadose zone water stock | mm | variable|
|`c` | positive real number | Effective scaling temperature (Oudin model) | Celcius | parameter|
|`cpmax` | positive real number | Effective canopy water stock capacity | mm | parameter|
|`f_cpmax` | positive real number | spatial factor for the `cpmax` parameter | unitless | subparameter|
|`f_cpmax_Alias` | positive real number | temporal factor for the `cpmax` parameter for LULC types (ex: `f_cpmax_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless | subparameter|
|`f_ksat` | positive real number | spatial factor for the `ksat` parameter | unitless | subparameter|
|`f_perv` | positive real number | spatial factor of perviousness(1 = 100% pervious) | unitless | subparameter|
|`f_rho` | positive real number | spatial factor for the `rho` parameter | unitless | subparameter|
|`f_roots` | positive real number | spatial factor for the `roots` parameter | unitless | subparameter|
|`f_roots_Alias` | positive real number | temporal factor for the `roots` parameter for LULC types (ex: `f_roots_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless | subparameter|
|`f_sfmax` | positive real number | spatial factor for the `sfmax` parameter | unitless | subparameter|
|`f_sfmax_Alias` | positive real number | temporal factor for the `sfmax` parameter for LULC types (ex: `f_sfmax_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless | subparameter|
|`h_max` | positive real number | Upper HAND threshold | m | parameter|
|`hand` | text | Keyword for Height Above the Nearest Drainage | - | keyword|
|`k` | positive real number | Effective residence time (Nash routing model) | d | parameter|
|`ksat` | positive real number | Effective soil hydraulic conductivity | mm/d | parameter|
|`lambda` | positive real number | Global saturation index | unitless | parameter|
|`load_N` | positive real number | Effective annual Nitrogen load | kgN / ha yr | subparameter|
|`load_P` | positive real number | Effective annual Phosphorous load | kgP / ha yr | subparameter|
|`lulc` | text | Keyword for Land use and Land cover types | - | keyword|
|`m` | positive real number | Exponential decay coefficient | mm | parameter|
|`n` | positive real number | Effective number of linear reservoir (Nash routing model) | unitless | parameter|
|`p05` | text | Keyword for `5% percentile` | - | keyword|
|`p95` | text | Keyword for `95% percentile` | - | keyword|
|`qo` | positive real number | Maximum baseflow | mm/d | parameter|
|`rho` | positive real number | Effective soil porosity | unitless | parameter|
|`roots` | positive real number | Effective root zone depth | mm | parameter|
|`sfmax` | positive real number | Effective surface water stock capacity | mm | parameter|
|`soils` | text | Keyword for soil types | - | keyword|
|`twi` | text | Keyword for Topographical Wetness Index | - | keyword|
|`usle_C` | positive real number | USLE `C` parameter | unitless | subparameter|
|`usle_K` | positive real number | USLE `K` parameter | ton h / (MJ mm) | subparameter|
|`usle_P` | positive real number | USLE `P` parameter | unitless | subparameter|
|`w` | positive real number | HAND to TWI dominance ratio | unitless | parameter|

### By category

#### Field
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`Alias` | text | Category alias (one-word only) | - | field|
|`Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | - | field|
|`Date` | date | Date of record | - | field|
|`Id` | unique integer number | Category numerical identifyier | - | field|
|`Max` | positive real number | Maximum value of parameter in confidence interval | - | field|
|`Min` | positive real number | Minimum value of parameter in confidence interval | - | field|
|`Name` | text | Category name | - | field|
|`Parameter` | text | Parameter name | - | field|
|`Set` | positive real number | Set value of parameter | - | field|

#### Variable
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`Cp` | positive real number | Canopy water stock | mm | variable|
|`D` | positive real number | Soil water deficit | mm | variable|
|`ET` | positive real number | Evapotranspiration  | mm/d | variable|
|`ET_obs` | positive real number | Observed Evapotranspiration  | mm/d | variable|
|`Flow` | positive real number | Streamflow | m3/s | variable|
|`Flow_obs` | positive real number | Observed streamflow | m3/s | variable|
|`IRA` | positive real number | Irrigation by aspersion | mm/d | variable|
|`IRI` | positive real number | Irrigation by inundation or dripping | mm/d | variable|
|`Inf` | positive real number | Infiltration | mm/d | variable|
|`Intc` | positive real number | Interception in canopy | mm/d | variable|
|`Ints` | positive real number | Interception in surface | mm/d | variable|
|`P` | positive real number | Precipitation | mm/d | variable|
|`PET` | positive real number | Potential evapotranspiration | mm/d | variable|
|`Q` | positive real number | Streamflow (specific) | mm/d | variable|
|`Q_obs` | positive real number | Observed specific streamflow | mm/d | variable|
|`Qb` | positive real number | Baseflow (specific) | mm/d | variable|
|`Qs` | positive real number | Stormflow (specific) | mm/d | variable|
|`Qv` | positive real number | Recharge | mm/d | variable|
|`R` | positive real number | Runoff | mm/d | variable|
|`RC` | positive real number | Runoff coeficient (100 * R/P) | % | variable|
|`RIE` | positive real number | Runoff by infiltration excess (Hortonian) | mm/d | variable|
|`RSE` | positive real number | Runoff by saturation excess (Dunnean) | mm/d | variable|
|`Sf` | positive real number | Surface water stock | mm | variable|
|`T` | positive real number | Mean daily temperature | Celcius | variable|
|`TF` | positive real number | Throughfall (effective precipitation) | mm/d | variable|
|`Vz` | positive real number | Vadose zone water stock | mm | variable|

#### Keyword
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`Max` | text | Keyword for `Maximum` | - | keyword|
|`Mean` | text | Keyword for `Mean` | - | keyword|
|`Med` | text | Keyword for `Median` | - | keyword|
|`Min` | text | Keyword for `Minimum` | - | keyword|
|`SD` | text | Keyword for `Standard Deviation` | - | keyword|
|`Stat` | text | Keyword for `statistic` | - | keyword|
|`Sum` | text | Keyword for `sum` | - | keyword|
|`Var` | text | Keyword for `variable` | - | keyword|
|`hand` | text | Keyword for Height Above the Nearest Drainage | - | keyword|
|`lulc` | text | Keyword for Land use and Land cover types | - | keyword|
|`p05` | text | Keyword for `5% percentile` | - | keyword|
|`p95` | text | Keyword for `95% percentile` | - | keyword|
|`soils` | text | Keyword for soil types | - | keyword|
|`twi` | text | Keyword for Topographical Wetness Index | - | keyword|

#### Parameter
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`Qt0` | positive real number | Streamflow (specific) when t=0 (initial condition) | mm/d | parameter|
|`c` | positive real number | Effective scaling temperature (Oudin model) | Celcius | parameter|
|`cpmax` | positive real number | Effective canopy water stock capacity | mm | parameter|
|`h_max` | positive real number | Upper HAND threshold | m | parameter|
|`k` | positive real number | Effective residence time (Nash routing model) | d | parameter|
|`ksat` | positive real number | Effective soil hydraulic conductivity | mm/d | parameter|
|`lambda` | positive real number | Global saturation index | unitless | parameter|
|`m` | positive real number | Exponential decay coefficient | mm | parameter|
|`n` | positive real number | Effective number of linear reservoir (Nash routing model) | unitless | parameter|
|`qo` | positive real number | Maximum baseflow | mm/d | parameter|
|`rho` | positive real number | Effective soil porosity | unitless | parameter|
|`roots` | positive real number | Effective root zone depth | mm | parameter|
|`sfmax` | positive real number | Effective surface water stock capacity | mm | parameter|
|`w` | positive real number | HAND to TWI dominance ratio | unitless | parameter|

#### Subparameter
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`f_cpmax` | positive real number | spatial factor for the `cpmax` parameter | unitless | subparameter|
|`f_cpmax_Alias` | positive real number | temporal factor for the `cpmax` parameter for LULC types (ex: `f_cpmax_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless | subparameter|
|`f_ksat` | positive real number | spatial factor for the `ksat` parameter | unitless | subparameter|
|`f_perv` | positive real number | spatial factor of perviousness(1 = 100% pervious) | unitless | subparameter|
|`f_rho` | positive real number | spatial factor for the `rho` parameter | unitless | subparameter|
|`f_roots` | positive real number | spatial factor for the `roots` parameter | unitless | subparameter|
|`f_roots_Alias` | positive real number | temporal factor for the `roots` parameter for LULC types (ex: `f_roots_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless | subparameter|
|`f_sfmax` | positive real number | spatial factor for the `sfmax` parameter | unitless | subparameter|
|`f_sfmax_Alias` | positive real number | temporal factor for the `sfmax` parameter for LULC types (ex: `f_sfmax_Fs` where `Fs` is the LULC Alias for `Forest`) | unitless | subparameter|
|`load_N` | positive real number | Effective annual Nitrogen load | kgN / ha yr | subparameter|
|`load_P` | positive real number | Effective annual Phosphorous load | kgP / ha yr | subparameter|
|`usle_C` | positive real number | USLE `C` parameter | unitless | subparameter|
|`usle_K` | positive real number | USLE `K` parameter | ton h / (MJ mm) | subparameter|
|`usle_P` | positive real number | USLE `P` parameter | unitless | subparameter|
