PROJECT_ID = package-registry-team11

main-service-dev:
	gcloud beta run services proxy main-service-dev --project $(PROJECT_ID) --port 9001
download-package-service-dev:
	gcloud beta run services proxy download-package-service-dev --project $(PROJECT_ID) --port 9002
fetch-directory-service-dev:
	gcloud beta run services proxy fetch-directory-service-dev --project $(PROJECT_ID) --port 9003
fetch-history-service-dev:
	gcloud beta run services proxy fetch-history-service-dev --project $(PROJECT_ID) --port 9004
ingest-package-service-dev:
	gcloud beta run services proxy ingest-package-service-dev --project $(PROJECT_ID) --port 9005
query-cost-service-dev:
	gcloud beta run services proxy query-cost-service-dev --project $(PROJECT_ID) --port 9006
rate-package-service-dev:
	gcloud beta run services proxy rate-package-service-dev --project $(PROJECT_ID) --port 9007
reset-system-service-dev:
	gcloud beta run services proxy reset-system-service-dev --project $(PROJECT_ID) --port 9008
search-package-service-dev:
	gcloud beta run services proxy search-package-service-dev --project $(PROJECT_ID) --port 9009
update-package-service-dev:
	gcloud beta run services proxy update-package-service-dev --project $(PROJECT_ID) --port 9010
upload-package-service-dev:
	gcloud beta run services proxy upload-package-service-dev --project $(PROJECT_ID) --port 9011

main-service-staging:
	gcloud beta run services proxy main-service-staging --project $(PROJECT_ID) --port 9101
download-package-service-staging:
	gcloud beta run services proxy download-package-service-staging --project $(PROJECT_ID) --port 9102
fetch-directory-service-staging:
	gcloud beta run services proxy fetch-directory-service-staging --project $(PROJECT_ID) --port 9103
fetch-history-service-staging:
	gcloud beta run services proxy fetch-history-service-staging --project $(PROJECT_ID) --port 9104
ingest-package-service-staging:
	gcloud beta run services proxy ingest-package-service-staging --project $(PROJECT_ID) --port 9105
query-cost-service-staging:
	gcloud beta run services proxy query-cost-service-staging --project $(PROJECT_ID) --port 9106
rate-package-service-staging:
	gcloud beta run services proxy rate-package-service-staging --project $(PROJECT_ID) --port 9107
reset-system-service-staging:
	gcloud beta run services proxy reset-system-service-staging --project $(PROJECT_ID) --port 9108
search-package-service-staging:
	gcloud beta run services proxy search-package-service-staging --project $(PROJECT_ID) --port 9109
update-package-service-staging:
	gcloud beta run services proxy update-package-service-staging --project $(PROJECT_ID) --port 9110
upload-package-service-staging:
	gcloud beta run services proxy upload-package-service-staging --project $(PROJECT_ID) --port 9111

main-service-prod:
	gcloud beta run services proxy main-service-prod --project $(PROJECT_ID) --port 9201
download-package-service-prod:
	gcloud beta run services proxy download-package-service-prod --project $(PROJECT_ID) --port 9202
fetch-directory-service-prod:
	gcloud beta run services proxy fetch-directory-service-prod --project $(PROJECT_ID) --port 9203
fetch-history-service-prod:
	gcloud beta run services proxy fetch-history-service-prod --project $(PROJECT_ID) --port 9204
ingest-package-service-prod:
	gcloud beta run services proxy ingest-package-service-prod --project $(PROJECT_ID) --port 9205
query-cost-service-prod:
	gcloud beta run services proxy query-cost-service-prod --project $(PROJECT_ID) --port 9206
rate-package-service-prod:
	gcloud beta run services proxy rate-package-service-prod --project $(PROJECT_ID) --port 9207
reset-system-service-prod:
	gcloud beta run services proxy reset-system-service-prod --project $(PROJECT_ID) --port 9208
search-package-service-prod:
	gcloud beta run services proxy search-package-service-prod --project $(PROJECT_ID) --port 9209
update-package-service-prod:
	gcloud beta run services proxy update-package-service-prod --project $(PROJECT_ID) --port 9210
upload-package-service-prod:
	gcloud beta run services proxy upload-package-service-prod --project $(PROJECT_ID) --port 9211