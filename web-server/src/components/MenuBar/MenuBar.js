import React from 'react';
import default_profile from '../../default-profile.png';
import { Navbar, Text, Dropdown, Avatar, Input, Link } from '@nextui-org/react';

const SearchIcon = ({size, fill, width = 24, height = 24, ...props}) => {
  return (
    <svg fill="none" height={size || height} viewBox="0 0 24 24" width={size || width} {...props}>
      <path
        d="M11.5 21a9.5 9.5 0 1 0 0-19 9.5 9.5 0 0 0 0 19ZM22 22l-2-2"
        stroke={fill}
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={2}
      />
    </svg>
  );
};

const AcmeLogo = () => (
  <svg
    className=""
    fill="none"
    height="36"
    viewBox="0 0 32 32"
    width="36"
    xmlns="http://www.w3.org/2000/svg"
  >
    <rect fill="var(--secondary)" height="100%" rx="16" width="100%" />
    <path
      clipRule="evenodd"
      d="M17.6482 10.1305L15.8785 7.02583L7.02979 22.5499H10.5278L17.6482 10.1305ZM19.8798 14.0457L18.11 17.1983L19.394 19.4511H16.8453L15.1056 22.5499H24.7272L19.8798 14.0457Z"
      fill="currentColor"
      fillRule="evenodd"
    />
  </svg>
);

const MenuBar = () => {
  const collapseItems = [
    "Dashboard",
    "Statistics",
    "Upload",
    "Registry",
  ];

  return (
    <Navbar maxWidth="fluid">
      <Navbar.Brand>
        <Navbar.Toggle aria-label="toggle navigation" />
        <AcmeLogo />
        <Text b color="inherit" hideIn="xs">
          ACME Package Registry
        </Text>
      </Navbar.Brand>
      <Navbar.Content>
        <Navbar.Item>
          <Input
            clearable
            contentLeft={
              <SearchIcon fill="var(--nextui-colors-accents6)" size={16} />
            }
            contentLeftStyling={false}
            css={{
              w: "100%",
              "@xsMax": {
                mw: "300px",
              },
              "& .nextui-input-content--left": {
                h: "100%",
                ml: "$4",
                dflex: "center",
              },
            }}
            placeholder="Search..."
          />
        </Navbar.Item>
        <Dropdown placement="bottom-right">
          <Dropdown.Trigger>
            <Avatar
              bordered
              as="button"
              color="primary"
              size="md"
              src={default_profile}
            />
          </Dropdown.Trigger>
          <Dropdown.Menu
            aria-label="User menu actions"
            color="primary"
          >
            <Dropdown.Item key="profile" css={{ height: "$18" }}>
              Signed in as
              kevin@example.com
            </Dropdown.Item>
            <Dropdown.Item key="settings" withDivider>
              Settings
            </Dropdown.Item>
            <Dropdown.Item key="logout" withDivider color="error">
              Log Out
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      </Navbar.Content>
      <Navbar.Collapse>
        {collapseItems.map((item, index) => (
          <Navbar.CollapseItem key={item}>
            <Link
              color="inherit"
              css={{
                minWidth: "100%",
              }}
              href="#"
            >
              {item}
            </Link>
          </Navbar.CollapseItem>
        ))}
      </Navbar.Collapse>
    </Navbar>
  );
}

export default MenuBar;