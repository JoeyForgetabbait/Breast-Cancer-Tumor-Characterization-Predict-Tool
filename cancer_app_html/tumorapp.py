{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3cb611c-a2ae-4a98-984a-fc7267a6f10e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the dependencies.\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "\n",
    "from flask import Flask, jsonify, render_template\n",
    "\n",
    "#################################################\n",
    "# Database Setup\n",
    "#################################################\n",
    "engine = create_engine(\"postgresql://postgres:postgres@localhost:5432/bart_train_routes\")\n",
    "\n",
    "# reflect an existing database into a new model\n",
    "Base = automap_base()\n",
    "# reflect the tables\n",
    "Base.prepare(autoload_with=engine)\n",
    "\n",
    "# Save references to each table\n",
    "bart_advisories = Base.classes.bart_advisories\n",
    "bart_crime = Base.classes.bart_crime_report_2021\n",
    "bart_route_info = Base.classes.bart_route_info\n",
    "bart_routes = Base.classes.bart_routes\n",
    "bart_stations = Base.classes.bart_station_info\n",
    "\n",
    "#################################################\n",
    "# Flask Setup\n",
    "#################################################\n",
    "app = Flask(__name__)\n",
    "\n",
    "#################################################\n",
    "# Flask Routes\n",
    "#################################################\n",
    "\n",
    "\n",
    "# creating welcome page\n",
    "# creating welcome page\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "\n",
    "@app.route(\"/data_docs\")\n",
    "def data_docs():\n",
    "    return \"\"\"Welcome to the BART Train Routes API! This will inform you about !<br/>\n",
    "        Available Routes:<br/>\n",
    "        /api/v1.0/advisories<br/>\n",
    "        /api/v1.0/crime_reports<br/>\n",
    "        /api/v1.0/route_info<br/>\n",
    "        /api/v1.0/stations<br/>\n",
    "        \"\"\"\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/advisories\")\n",
    "def advisories():\n",
    "    # Create our session (link) from Python to the DB\n",
    "    session = Session(engine)\n",
    "    # Query all advisories\n",
    "    results = session.query(bart_advisories.id, bart_advisories.station, bart_advisories.description, bart_advisories.date, bart_advisories.time).all()\n",
    "    # Create a dictionary from the row data and append to a list of all_advisories\n",
    "    all_advisories = []\n",
    "    for id, station, description, date, time in results:\n",
    "        advisory_dict = {}\n",
    "        advisory_dict[\"ID\"] = id\n",
    "        advisory_dict[\"Station\"] = station\n",
    "        advisory_dict[\"Description\"] = description\n",
    "        advisory_dict[\"Date\"] = date\n",
    "        advisory_dict[\"Time\"] = time\n",
    "        all_advisories.append(advisory_dict)\n",
    "    session.close()\n",
    "    return jsonify(all_advisories)\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/crime_reports\")\n",
    "def crime_reports():\n",
    "    # Create our session (link) from Python to the DB\n",
    "    session = Session(engine)\n",
    "    results = session.query(bart_crime.id, bart_crime.location, bart_crime.date, bart_crime.time, bart_crime.charge_description)\n",
    "    all_crime_reports = []\n",
    "    for id, location, date, time, charge_description in results:\n",
    "        crime_dict = {}\n",
    "        crime_dict[\"ID\"] = id\n",
    "        crime_dict[\"Location\"] = location\n",
    "        crime_dict[\"Charge Description\"] = charge_description\n",
    "        crime_dict[\"Date\"] = date\n",
    "        crime_dict[\"Time\"] = time\n",
    "        all_crime_reports.append(crime_dict)\n",
    "    session.close()\n",
    "    return jsonify(all_crime_reports)\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/crime_count_<station_id>\")\n",
    "def crime_count(station_id):\n",
    "    # Create our session (link) from Python to the DB\n",
    "    session = Session(engine)\n",
    "    station_name = session.query(bart_stations.name).filter(bart_stations.id == station_id).first()[0]\n",
    "    print(station_name)\n",
    "    results = session.query(bart_crime.charge_description, func.count(bart_crime.id)).filter(bart_crime.location.like(\"%\" + station_name + \"%\")).group_by(bart_crime.charge_description).order_by(func.count(bart_crime.id).desc()).limit(5).all()\n",
    "    # bart_crime.location == station_name).\n",
    "    results = [{\"desc\": row[0], \"count\": row[1]} for row in results]\n",
    "    session.close()\n",
    "    return jsonify(results)\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/route_info\")\n",
    "def route_info():\n",
    "    session = Session(engine)\n",
    "    # Query all route info\n",
    "    results = session.query(bart_route_info.id, bart_route_info.route_id, bart_route_info.name, bart_route_info.abbr, bart_route_info.color, bart_route_info.config).all()\n",
    "    # Create a dictionary from the row data and append to a list of all_route_info\n",
    "    all_route_info = []\n",
    "    for id, route_id, name, abbr, color, config in results:\n",
    "        route_dict = {}\n",
    "        route_dict[\"ID\"] = id\n",
    "        route_dict[\"Route ID\"] = route_id\n",
    "        route_dict[\"Name\"] = name\n",
    "        route_dict[\"Abbreviation\"] = abbr\n",
    "        route_dict[\"Color\"] = color\n",
    "        route_dict[\"Config\"] = config\n",
    "        all_route_info.append(route_dict)\n",
    "    session.close()\n",
    "    return jsonify(all_route_info)\n",
    "\n",
    "\n",
    "# @app.route('/api/v1.0/routes')\n",
    "# def routes():\n",
    "#     session=Session(engine)\n",
    "#     # Query all route\n",
    "#     results = session.query(bart_routes.routes, bart_routes.id, bart_routes.route_id, bart_routes.routes_name,bart_routes.route.abbr, bart_routes.routes_color, bart_routes.routes_config).all()\n",
    "\n",
    "#     # Create a dictionary from the row data and append to a list of all_route_info\n",
    "#     all_routes = []\n",
    "#     for routes, id, route_id, route_name, route_abbr, route_color, route_config in results:\n",
    "#         route_dict = {}\n",
    "#         route_dict[\"Routes\"] = routes\n",
    "#         route_dict[\"ID\"] = id\n",
    "#         route_dict[\"Route ID\"] = route_id\n",
    "#         route_dict[\"Route Name\"] = route_name\n",
    "#         route_dict[\"Route Abbreviation\"] = route_abbr\n",
    "#         route_dict[\"Route Color\"] = route_color\n",
    "#         route_dict[\"Route Config\"] = route_config\n",
    "#         all_routes.append(route_dict)\n",
    "#     session.close()\n",
    "#     return jsonify(all_routes)\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    session = Session(engine)\n",
    "    # Query all stations\n",
    "    results = session.query(bart_stations.id, bart_stations.name, bart_stations.abbr, bart_stations.latitude, bart_stations.longitude, bart_stations.address, bart_stations.city, bart_stations.zipcode).all()\n",
    "    # Create a dictionary from the row data and append to a list of all_stations\n",
    "    all_stations = []\n",
    "    for id, name, abbr, latitude, longitude, bart_address, city, zipcode in results:\n",
    "        station_dict = {}\n",
    "        station_dict[\"ID\"] = id\n",
    "        station_dict[\"Name\"] = name\n",
    "        station_dict[\"Abbreviation\"] = abbr\n",
    "        station_dict[\"Latitude\"] = latitude\n",
    "        station_dict[\"Longitude\"] = longitude\n",
    "        station_dict[\"BART Address\"] = bart_address\n",
    "        station_dict[\"City\"] = city\n",
    "        station_dict[\"Zipcode\"] = zipcode\n",
    "        all_stations.append(station_dict)\n",
    "\n",
    "        # all_stations=[{'station id':station_id,}for station_id, station_name, station_abbr, station_latitude, station_longitude,bart_address in results]\n",
    "    session.close()\n",
    "    return jsonify(all_stations)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}