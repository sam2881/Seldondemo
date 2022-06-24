



FROM python:3.9-slim
# FROM itx-bke.artifactrepo.jnj.com/recommendation-model:V1

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
 
# Define environment variable
ENV MODEL_NAME RecommendationModel
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0
 
CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE --persistence $PERSISTENCE
