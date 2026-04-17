from src.data.build_player_master import main as build_player_master_main
from src.data.build_player_derived_stats import main as build_player_derived_stats_main
from src.data.clean_player_manual_attributes import main as clean_player_manual_main
from src.data.build_player_profile_master import main as build_player_profile_main
from src.utils.logger import get_logger

logger = get_logger(__name__)


def run_player_profile_pipeline():
    logger.info("Starting player profile pipeline...")
    build_player_master_main()
    clean_player_manual_main()
    build_player_derived_stats_main()
    build_player_profile_main()
    logger.info("Player profile pipeline completed successfully.")


if __name__ == "__main__":
    run_player_profile_pipeline()