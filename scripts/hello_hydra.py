"""Learning script: see Hydra in action.

Run examples:
    python scripts/hello_hydra.py
    python scripts/hello_hydra.py model=nemotron_nano
    python scripts/hello_hydra.py inference=sampling
    python scripts/hello_hydra.py +experiment=baseline
    python scripts/hello_hydra.py inference.temperature=0.3
    python scripts/hello_hydra.py project.seed=123
    python scripts/hello_hydra.py --help
"""

import hydra
from omegaconf import DictConfig, OmegaConf

from src.tracking.experiment import Experiment
from src.utils.logging import get_logger, setup_logging
from src.utils.seed import set_seed


@hydra.main(version_base="1.3", config_path="../configs", config_name="config")
def main(cfg: DictConfig) -> None:
    """Demonstrate Hydra config composition + project utilities."""
    # 1. Set up logging
    setup_logging(level=cfg.project.log_level)
    logger = get_logger(__name__)

    logger.info("=" * 60)
    logger.info("Hello, Hydra!")
    logger.info("=" * 60)

    # 2. Fix randomness
    set_seed(cfg.project.seed)
    logger.info("Random seed set to %d", cfg.project.seed)

    # 3. Create an experiment
    exp = Experiment.create(
        outputs_root=cfg.paths.outputs,
        custom_name=getattr(cfg.tracking, "experiment_id", None) or "demo",
    )
    logger.info("Experiment ID: %s", exp.exp_id)
    logger.info("Output dir: %s", exp.output_dir)
    logger.info("Git commit: %s", exp.git_commit or "<not in a git repo>")

    # 4. Show what was composed
    logger.info("")
    logger.info("Composed config:")
    logger.info("  model.name        = %s", cfg.model.name)
    logger.info("  prompt.strategy   = %s", cfg.prompt.strategy)
    logger.info("  inference.strategy = %s", cfg.inference.strategy)
    logger.info("  inference.temperature = %s", cfg.inference.temperature)
    logger.info("  data.name         = %s", cfg.data.name)
    logger.info("  data.n_samples    = %s", cfg.data.n_samples)

    # 5. Save the full config snapshot to the experiment directory
    config_snapshot_path = exp.output_dir / "config.yaml"
    config_snapshot_path.write_text(OmegaConf.to_yaml(cfg), encoding="utf-8")
    logger.info("")
    logger.info("Full config saved to: %s", config_snapshot_path)


if __name__ == "__main__":
    main()
