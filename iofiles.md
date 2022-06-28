# IO files
 - [Imported files](https://github.com/ipo-exe/tklab/blob/main/iofiles.md#imported-files)
 - [Output files](https://github.com/ipo-exe/tklab/blob/main/iofiles.md#output-files)
# Imported files
These files must be prepared and sourced by the user. Samples are provided for proper formatting.
## `param_lulc.txt`
 - **Description**: Table of LULC parameters;
 - **Source**: imported by user;
 - **Format**: Data Table;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:
	 - `Id ` [unique integer number]: Category numerical identifyier [-];
	 - ` Name ` [text]: Category name [-];
	 - ` Alias ` [text]: Category alias (one-word only) [-];
	 - ` Color ` [text]: CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). [-];
	 - ` f_cpmax ` [positive real number]: spatial factor for the `cpmax` parameter [unitless];
	 - ` f_sfmax ` [positive real number]: spatial factor for the `sfmax` parameter [unitless];
	 - ` f_roots ` [positive real number]: spatial factor for the `roots` parameter [unitless];
	 - ` f_perv ` [positive real number]: spatial factor of perviousness(1 = 100% pervious) [unitless];
	 - ` usle_C ` [positive real number]: USLE `C` parameter [unitless];
	 - ` usle_P ` [positive real number]: USLE `P` parameter [unitless];
	 - ` load_N ` [positive real number]: Effective annual Nitrogen load [KgN / yr];
	 - ` load_P` [positive real number]: Effective annual Phosphorous load [kgP / yr];
 - **File sample**: [param_lulc.txt](https://github.com/ipo-exe/tklab/blob/main/samples/param_lulc.txt);
 - **Formating example**:

## `param_soils.txt`
 - **Description**: Table of Soils parameters;
 - **Source**: imported by user;
 - **Format**: Data Table;
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:
	 - `Id ` [unique integer number]: Category numerical identifyier [-];
	 - ` Name ` [text]: Category name [-];
	 - ` Alias ` [text]: Category alias (one-word only) [-];
	 - ` Color ` [text]: CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). [-];
	 - ` f_ksat ` [positive real number]: spatial factor for the `ksat` parameter [unitless];
	 - ` f_rho ` [positive real number]: spatial factor for the `rho` parameter [unitless];
	 - ` usle_K` [positive real number]: USLE `K` parameter [ton h / (MJ mm)];
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
	 - `Parameter ` [text]: Parameter name [-];
	 - ` Set ` [positive real number]: Set value of parameter [-];
	 - ` Min ` [positive real number]: Minimum value of parameter in confidence interval [-];
	 - ` Max` [positive real number]: Maximum value of parameter in confidence interval [-];
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

## `map_ET_obs_{Date}.asc`
 - **Description**: Map of observed Evapotranspiration in Date={Date};
 - **Source**: imported by user;
 - **Format**: Raster Map;
 - **Requirements**:
	 - Void cells value: not allowed - all grid cells must be filled with data;
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
 - **File sample**: [map_ET_obs_{Date}.asc](https://github.com/ipo-exe/tklab/blob/main/samples/map_ET_obs_{Date}.asc);
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
	 - `Date ` [date]: Date of record [-];
	 - ` P ` [positive real number]: Precipitation [mm/d];
	 - ` T ` [positive real number]: Mean daily temperature [Celcius];
	 - ` IRA ` [positive real number]: Irrigation by aspersion [mm/d];
	 - ` IRI` [positive real number]: Irrigation by inundation or dripping [mm/d];
 - **Optional Fields**:
	 - `Q_obs ` [positive real number]: Observed specific streamflow [mm/d];
	 - ` Flow_obs ` [positive real number]: Observed streamflow [m3/s];
	 - ` ET_obs ` [positive real number]: Observed Evapotranspiration  [mm/d];
	 - ` f_cpmax_{Alias} ` [positive real number]: temporal factor for the `cpmax` parameter in LULC where `Alias={Alias}` [unitless];
	 - ` f_sfmax_{Alias} ` [positive real number]: temporal factor for the `sfmax` parameter in LULC where `Alias={Alias}` [unitless];
	 - ` f_roots_{Alias}` [positive real number]: temporal factor for the `roots` parameter in LULC where `Alias={Alias}` [unitless];
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
```# Output files
These files are generated by the program.