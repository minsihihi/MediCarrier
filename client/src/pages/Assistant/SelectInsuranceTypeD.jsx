import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import ProgressIndicator from "../../components/ProgressIndicator";

const PageContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #fafafa;
`;

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 393px;
  height: 792px;
  margin: 0;
  background: #ffffff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding-bottom: 95px;
`;

const Title = styled.h1`
  font-family: Pretendard;
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
  text-align: left;
  line-height: 1.5;
  align-self: flex-start;
  margin-left: 20px;
  margin-top: 51px;
`;

const Subtitle = styled.p`
  color: #000;
  font-family: Pretendard;
  font-size: 14px;
  font-style: normal;
  font-weight: 300;
  line-height: normal;
  letter-spacing: -0.439px;
  margin-bottom: 40px;
  margin-left: 20px;
  align-self: flex-start;
`;

const SpecialtyContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  gap: 10px;
  margin-bottom: 20px;
  width: 90%;
  margin-left: 20px;
`;

const Specialty = styled.button`
  font-family: Pretendard;
  padding: 10px 20px;
  font-size: 14px;
  font-weight: ${(props) => (props.selected ? "bold" : "normal")};
  color: #000000;
  background-color: ${(props) =>
    props.selected ? "rgba(255, 249, 119, 0.40)" : "#F8F8F8"};
  border: ${(props) =>
    props.selected ? "1px solid var(--pointyellow, #FFF977)" : "none"};
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
`;

const ButtonContainer = styled.div`
  display: flex;
  justify-content: center;
  gap: 11px;
  width: 100%;
  padding: 0 20px;
`;

const Button = styled.button`
  font-family: Pretendard;
  width: 171px;
  height: 51px;
  padding: 10px 20px;
  font-size: 16px;
  color: ${(props) => (props.primary ? "#FFFFFF" : "#000000")};
  background-color: ${(props) => (props.primary ? "#4A7DFF" : "#F8F8F8")};
  border: none;
  border-radius: 16px;
  cursor: pointer;
  margin-top: 266px;
`;

const insuranceTypes = ["입원", "통원", "후유장애", "수술", "진단"];

function SelectInsuranceTypeD() {
  const navigate = useNavigate();
  const [selected, setSelected] = useState(null);

  const handleSelect = (type) => {
    setSelected(type);
  };

  const handleNext = () => {
    if (selected) {
      switch (selected) {
        case "입원":
        case "후유장애":
        case "수술":
          navigate("/document-guide");
        case "통원":
          navigate("/select-paid");
        case "진단":
          navigate("/select-claim");
          break;
        default:
          break;
      }
    }
  };

  return (
    <PageContainer>
      <Container>
        <ProgressIndicator step={3} />
        <Title>어떤 보험 청구가 필요하신가요?</Title>
        <Subtitle>
          조건을 선택해주시면 청구 시 필요한 서류를 안내해드릴게요
        </Subtitle>
        <SpecialtyContainer>
          {insuranceTypes.slice(0, 2).map((type, index) => (
            <Specialty
              key={index}
              selected={selected === type}
              onClick={() => handleSelect(type)}
            >
              {type}
            </Specialty>
          ))}
        </SpecialtyContainer>
        <SpecialtyContainer>
          {insuranceTypes.slice(2).map((type, index) => (
            <Specialty
              key={index}
              selected={selected === type}
              onClick={() => handleSelect(type)}
            >
              {type}
            </Specialty>
          ))}
        </SpecialtyContainer>
        <ButtonContainer>
          <Button onClick={() => navigate(-1)} primary={false}>
            이전
          </Button>
          <Button onClick={handleNext} primary={true} disabled={!selected}>
            다음
          </Button>
        </ButtonContainer>
      </Container>
    </PageContainer>
  );
}

export default SelectInsuranceTypeD;