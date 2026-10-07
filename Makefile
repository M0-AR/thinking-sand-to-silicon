.PHONY: all exp01 exp02 exp03 exp04 exp05 test compose

all: exp01 exp02 exp03 exp04 exp05

exp01:
	python3 experiments/01_tta_semantics.py
exp02:
	python3 experiments/02_pipelining_timing.py
exp03:
	python3 experiments/03_openlane_flow_model.py
exp04:
	python3 experiments/04_mpw_economics_live.py
exp05:
	python3 experiments/05_verification_bringup.py

test:
	pytest -q

compose:
	docker compose up --build
