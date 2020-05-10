from datetime import datetime
from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
crest = {
	"rest_name" : "PruebaRest",
	"email" : "pruebarest@test.es",
	"logo" : "./src/logoprueba.png",
}
RESTAURANTES = {
	"BKING": {
		"rest_name" : "Burguer King",
		"rest_id" : 1,
		"logo" : "./src/bklogo.png",
		"qr" : "./src/bkqr.png",
		"email" : "bk@restaurant.es",
		"platos" :[
			{
				"name" : "bigKing",
				"id" : 1,
				"price" : 5.5,
				"description": "deliciosa hamburguesa",
				"imagen": "./src/bigking.png",
				"categoria":[
					#/*entrante*/
					True,
					#/*ensalada*/
					False,
					#/*ave*/
					False,
					#/*carne*/
					True,
					#/*bebida*/
					False
				],
				"alergenos":[
					#/*gluten*/
					True,
					#/*leche*/
					True,
					#/*huevo*/
					True,
					#/pescado*/
					False
				],
				"meGusta": 4,
				"horario":[
					#/*apertura*/
					"9:00",
					#/*cierre*/
					"3:00"
				]
			},
			{
				"name" : "bigChicken",
				"id" : 2,
				"price" : 6.5,
				"description": "deliciosa hamburguesa de pollo",
				"imagen": "./src/bigchicken.png",
				"categoria":[
					#/*entrante*/
					True,
					#/*ensalada*/
					True,
					#/*ave*/
					True,
					#/*carne*/
					False,
					#/*bebida*/
					False
				],
				"alergenos":[
					#/*gluten*/
					True,
					#/*leche*/
					True,
					#/*huevo*/
					True,
					#/pescado*/
					False
				],
				"meGusta": 4,
				"horario":[
					#/*apertura*/
					"9:00",
					#/*cierre*/
					"3:00"
				]
			}
		],
		"timestamp": get_timestamp()
	},
	"BKING2": {
		"rest_name" : "Burguer King2",
		"rest_id" : 2,
		"logo" : "./src/bklogo.png",
		"qr" : "./src/bkqr.png",
		"email" : "bk@restaurant.es",
		"platos" :[
			{
				"name" : "bigKing",
				"id" : 1,
				"price" : 5.5,
				"description": "deliciosa hamburguesa",
				"imagen": "./src/bigking.png",
				"categoria":[
					#/*entrante*/
					True,
					#/*ensalada*/
					False,
					#/*ave*/
					False,
					#/*carne*/
					True,
					#/*bebida*/
					False
				],
				"alergenos":[
					#/*gluten*/
					True,
					#/*leche*/
					True,
					#/*huevo*/
					True,
					#/pescado*/
					False
				],
				"meGusta": 4,
				"horario":[
					#/*apertura*/
					"9:00",
					#/*cierre*/
					"3:00"
				]
			},
			{
				"name" : "bigChicken",
				"id" : 2,
				"price" : 6.5,
				"description": "deliciosa hamburguesa de pollo",
				"imagen": "./src/bigchicken.png",
				"categoria":[
					#/*entrante*/
					True,
					#/*ensalada*/
					True,
					#/*ave*/
					True,
					#/*carne*/
					False,
					#/*bebida*/
					False
				],
				"alergenos":[
					#/*gluten*/
					True,
					#/*leche*/
					True,
					#/*huevo*/
					True,
					#/pescado*/
					False
				],
				"meGusta": 4,
				"horario":[
					#/*apertura*/
					"9:00",
					#/*cierre*/
					"3:00"
				]
			}
		],
		"timestamp": get_timestamp()
	}
}

def read_all():
	"""
	responde a una llamada a api/restaurant/
	con la lista completa de restaurantes
	"""
	#creando la lista de restaurantes
	return [RESTAURANTES[key] for key in sorted(RESTAURANTES.keys())]

def create(restaurant):
	"""
	crea un restaurante y lo añade a la lista de restaurantes
	:param restaurant: restaurante a crear en la estructura
	:return: 201 on success, 406 on restaurant exists
	"""
	rest_name = restaurant.get("rest_name",None)
	email = restaurant.get("email", None)
	logo = restaurant.get("logo", None)

	# exite el restaurante?
	if rest_name not in RESTAURANTES and email is not None and logo is not None:
		RESTAURANTES[rest_name] = {
			"rest_name" : rest_name,
			"email" : email,
			"logo" : logo,
			"timestamp" : get_timestamp()

		}
		return make_response(
			"{rest_name} succesfully created".format(rest_name=rest_name),
			201
		)
	else:
		abort(
			406,
			"Restaurant with restaurant name {rest_name} already exists".format(rest_name=rest_name)
		)
