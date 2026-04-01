from src.api_service import get_study_advice


def test_get_study_advice_returns_expected_structure():
    result = get_study_advice()

    assert isinstance(result, dict)
    assert "study_tip" in result
    assert "external_advice" in result
    assert "source" in result

    assert isinstance(result["study_tip"], str)
    assert isinstance(result["external_advice"], str)
    assert isinstance(result["source"], str)

    assert len(result["study_tip"]) > 0
    assert len(result["external_advice"]) > 0
    assert len(result["source"]) > 0